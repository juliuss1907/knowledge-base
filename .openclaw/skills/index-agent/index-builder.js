#!/usr/bin/env node
/**
 * Index Agent - Full Rebuild Mode
 * Scans all wiki files, builds tag and topic indexes
 */

const fs = require('fs');
const path = require('path');

const WIKI_ROOT = '/home/julius/knowledge-base/wiki';
const TAGS_FILE = '/home/julius/knowledge-base/TAGS.md';

// Parse YAML frontmatter
function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  
  const yaml = match[1];
  const result = {};
  
  for (const line of yaml.split('\n')) {
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) continue;
    
    const key = line.slice(0, colonIndex).trim();
    let value = line.slice(colonIndex + 1).trim();
    
    // Parse arrays
    if (value.startsWith('[') && value.endsWith(']')) {
      value = value.slice(1, -1).split(',').map(v => v.trim()).filter(v => v);
    } else if (value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    } else if (value.startsWith("'") && value.endsWith("'")) {
      value = value.slice(1, -1);
    }
    
    result[key] = value;
  }
  
  return result;
}

// Derive title from slug
function deriveTitle(slug) {
  return slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

// Load allowed tags from TAGS.md
function loadAllowedTags() {
  const content = fs.readFileSync(TAGS_FILE, 'utf8');
  const mainTags = [];
  const subTags = [];
  
  let inPoolA = false;
  let inPoolB = false;
  
  for (const line of content.split('\n')) {
    if (line.includes('Pool A')) inPoolA = true;
    if (line.includes('Pool B')) { inPoolA = false; inPoolB = true; }
    if (line.startsWith('| `#') && (inPoolA || inPoolB)) {
      const match = line.match(/`#(\w+)`/);
      if (match) {
        if (inPoolA) mainTags.push(match[1]);
        else if (inPoolB) subTags.push(match[1]);
      }
    }
  }
  
  return { main: mainTags, sub: subTags };
}

// Main function
async function buildIndexes() {
  console.log('=== Index Agent - Full Rebuild ===\n');
  
  const allowedTags = loadAllowedTags();
  console.log('Allowed main tags:', allowedTags.main.join(', '));
  console.log('Allowed sub tags:', allowedTags.sub.join(', '));
  console.log('');
  
  // Find all wiki files
  const conceptsDir = path.join(WIKI_ROOT, 'concepts');
  const sourcesDir = path.join(WIKI_ROOT, 'sources');
  
  const conceptFiles = fs.readdirSync(conceptsDir).filter(f => f.endsWith('.md'));
  const sourceFiles = fs.readdirSync(sourcesDir).filter(f => f.endsWith('.md'));
  
  console.log(`Found ${conceptFiles.length} concept files, ${sourceFiles.length} source files`);
  console.log('');
  
  // Parse all files
  const files = [];
  const errors = [];
  
  for (const file of conceptFiles) {
    const content = fs.readFileSync(path.join(conceptsDir, file), 'utf8');
    const fm = parseFrontmatter(content);
    
    if (!fm) {
      errors.push({ file: `concepts/${file}`, error: 'No frontmatter' });
      continue;
    }
    
    files.push({
      path: `concepts/${file}`,
      slug: file.replace('.md', ''),
      type: fm.type || 'concept',
      main_tag: fm.main_tag,
      sub_tags: Array.isArray(fm.sub_tags) ? fm.sub_tags : [],
      topic: fm.topic,
      title: fm.title || deriveTitle(file.replace('.md', ''))
    });
  }
  
  for (const file of sourceFiles) {
    const content = fs.readFileSync(path.join(sourcesDir, file), 'utf8');
    const fm = parseFrontmatter(content);
    
    if (!fm) {
      errors.push({ file: `sources/${file}`, error: 'No frontmatter' });
      continue;
    }
    
    files.push({
      path: `sources/${file}`,
      slug: file.replace('.md', ''),
      type: fm.type || 'source',
      main_tag: fm.main_tag,
      sub_tags: Array.isArray(fm.sub_tags) ? fm.sub_tags : [],
      topic: fm.topic,
      title: fm.title || deriveTitle(file.replace('.md', '').replace('src_', ''))
    });
  }
  
  console.log(`Successfully parsed ${files.length} files`);
  if (errors.length > 0) {
    console.log(`Errors: ${errors.length} files skipped`);
  }
  console.log('');
  
  // Build tag index
  const tagIndex = {};
  const invalidTags = [];
  
  for (const file of files) {
    // Main tag
    if (file.main_tag) {
      if (!allowedTags.main.includes(file.main_tag)) {
        invalidTags.push({ file: file.path, tag: file.main_tag, type: 'main' });
      } else {
        if (!tagIndex[file.main_tag]) tagIndex[file.main_tag] = { concepts: [], sources: [] };
        if (file.type === 'concept') tagIndex[file.main_tag].concepts.push(file);
        else tagIndex[file.main_tag].sources.push(file);
      }
    }
    
    // Sub tags
    for (const tag of file.sub_tags) {
      if (!allowedTags.sub.includes(tag)) {
        invalidTags.push({ file: file.path, tag, type: 'sub' });
      } else {
        if (!tagIndex[tag]) tagIndex[tag] = { concepts: [], sources: [] };
        if (file.type === 'concept') tagIndex[tag].concepts.push(file);
        else tagIndex[tag].sources.push(file);
      }
    }
  }
  
  // Sort files within each tag
  for (const tag of Object.keys(tagIndex)) {
    tagIndex[tag].concepts.sort((a, b) => a.slug.localeCompare(b.slug));
    tagIndex[tag].sources.sort((a, b) => a.slug.localeCompare(b.slug));
  }
  
  console.log(`Built index for ${Object.keys(tagIndex).length} tags`);
  if (invalidTags.length > 0) {
    console.log(`Invalid tags found: ${invalidTags.length}`);
  }
  console.log('');
  
  // Calculate co-occurrence
  const coOccurrence = {};
  
  for (const file of files) {
    const fileTags = [file.main_tag, ...file.sub_tags].filter(Boolean);
    for (let i = 0; i < fileTags.length; i++) {
      for (let j = i + 1; j < fileTags.length; j++) {
        const pair = [fileTags[i], fileTags[j]].sort();
        const key = pair.join('|');
        coOccurrence[key] = (coOccurrence[key] || 0) + 1;
      }
    }
  }
  
  // Build per-tag co-occurrence
  const tagCoOccur = {};
  for (const tag of Object.keys(tagIndex)) {
    const pairs = [];
    for (const [key, count] of Object.entries(coOccurrence)) {
      const [t1, t2] = key.split('|');
      if (t1 === tag) pairs.push([t2, count]);
      else if (t2 === tag) pairs.push([t1, count]);
    }
    pairs.sort((a, b) => b[1] - a[1]);
    tagCoOccur[tag] = pairs.slice(0, 5);
  }
  
  // Build topic index
  const topicIndex = {};
  
  for (const file of files) {
    if (!file.topic) continue;
    if (!topicIndex[file.topic]) topicIndex[file.topic] = { concepts: [], sources: [] };
    if (file.type === 'concept') topicIndex[file.topic].concepts.push(file);
    else topicIndex[file.topic].sources.push(file);
  }
  
  // Sort files within each topic
  for (const topic of Object.keys(topicIndex)) {
    topicIndex[topic].concepts.sort((a, b) => a.slug.localeCompare(b.slug));
    topicIndex[topic].sources.sort((a, b) => a.slug.localeCompare(b.slug));
  }
  
  console.log(`Built index for ${Object.keys(topicIndex).length} topics`);
  console.log('');
  
  // Write tag index files
  const tagDir = path.join(WIKI_ROOT, 'tag');
  if (!fs.existsSync(tagDir)) fs.mkdirSync(tagDir, { recursive: true });
  
  const today = new Date().toISOString().split('T')[0];
  
  for (const [tag, data] of Object.entries(tagIndex)) {
    const totalFiles = data.concepts.length + data.sources.length;
    
    let content = `---
type: index
level: 3
scope: tag
parent: "[[tag]]"
tag: ${tag}
auto_generated: true
last_updated: ${today}
---

# Tag: #${tag}

## Parent

- [[tag]]

## Stats

- Total files: ${totalFiles}
- Sources: ${data.sources.length}
- Concepts: ${data.concepts.length}
- Last updated: ${today}

## Files with this tag

`;
    
    // Merge and sort all items
    const allItems = [
      ...data.concepts.map(f => ({ ...f, ftype: 'concept' })),
      ...data.sources.map(f => ({ ...f, ftype: 'source' }))
    ].sort((a, b) => a.slug.localeCompare(b.slug));
    
    for (const item of allItems) {
      content += `- [[${item.slug}]] — ${item.title} (${item.ftype})\n`;
    }
    
    // Co-occurring tags
    if (tagCoOccur[tag] && tagCoOccur[tag].length > 0) {
      content += `\n## Co-occurring tags\n\n`;
      for (const [otherTag, count] of tagCoOccur[tag]) {
        const unit = count === 1 ? 'co-occurrence' : 'co-occurrences';
        content += `- [[${otherTag}]] — ${count} ${unit}\n`;
      }
    }
    
    fs.writeFileSync(path.join(tagDir, `${tag}.md`), content);
  }
  
  console.log(`✓ Wrote ${Object.keys(tagIndex).length} tag index files`);
  
  // Write topic index files
  const topicDir = path.join(WIKI_ROOT, 'topic');
  if (!fs.existsSync(topicDir)) fs.mkdirSync(topicDir, { recursive: true });
  
  for (const [topic, data] of Object.entries(topicIndex)) {
    let content = `---
type: index
scope: topic
parent: "[[topic]]"
topic: ${topic}
auto_generated: true
last_updated: ${today}
---

# Topic: ${topic}

Auto-generated index of all content with topic \`${topic}\`.

Last updated: ${new Date().toISOString().replace('T', ' ').slice(0, 19)}

---

## Concepts (${data.concepts.length})

`;
    
    for (const file of data.concepts) {
      const subs = file.sub_tags.map(t => `#${t}`).join(', ');
      content += `- [[${file.slug}]] — main: #${file.main_tag}, sub: [${subs}]\n`;
    }
    
    content += `\n## Sources (${data.sources.length})\n\n`;
    
    for (const file of data.sources) {
      const subs = file.sub_tags.map(t => `#${t}`).join(', ');
      content += `- [[${file.slug}]] — main: #${file.main_tag}, sub: [${subs}]\n`;
    }
    
    fs.writeFileSync(path.join(topicDir, `${topic}.md`), content);
  }
  
  console.log(`✓ Wrote ${Object.keys(topicIndex).length} topic index files`);
  
  // Update tag.md master index
  const tagMdPath = path.join(tagDir, 'tag.md');
  if (fs.existsSync(tagMdPath)) {
    let tagMdContent = fs.readFileSync(tagMdPath, 'utf8');
    
    // Update Stats section
    const mainTagsCount = allowedTags.main.length;
    const subTagsCount = Object.keys(tagIndex).length - mainTagsCount;
    
    // Count most used tags
    const tagCounts = {};
    for (const [tag, data] of Object.entries(tagIndex)) {
      tagCounts[tag] = data.concepts.length + data.sources.length;
    }
    const top3 = Object.entries(tagCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 3)
      .map(([tag, count]) => `#${tag} (${count})`)
      .join(', ');
    
    // Update stats in content
    tagMdContent = tagMdContent.replace(
      /- Total tags: \d+/,
      `- Total tags: ${Object.keys(tagIndex).length}`
    );
    tagMdContent = tagMdContent.replace(
      /- Main tags: \d+/,
      `- Main tags: ${mainTagsCount}`
    );
    tagMdContent = tagMdContent.replace(
      /- Sub tags: \d+/,
      `- Sub tags: ${subTagsCount}`
    );
    tagMdContent = tagMdContent.replace(
      /- Most used: .*/,
      `- Most used: ${top3}`
    );
    tagMdContent = tagMdContent.replace(
      /- Last updated: \d{4}-\d{2}-\d{2}/,
      `- Last updated: ${today}`
    );
    
    fs.writeFileSync(tagMdPath, tagMdContent);
    console.log('✓ Updated wiki/tag/tag.md');
  }
  
  // Clean up orphaned index files
  const existingTagFiles = fs.readdirSync(tagDir).filter(f => f.endsWith('.md') && f !== 'tag.md');
  const currentTags = Object.keys(tagIndex);
  let deletedTags = 0;
  
  for (const file of existingTagFiles) {
    const tag = file.replace('.md', '');
    if (!currentTags.includes(tag)) {
      fs.unlinkSync(path.join(tagDir, file));
      deletedTags++;
    }
  }
  
  const existingTopicFiles = fs.existsSync(topicDir) ? fs.readdirSync(topicDir).filter(f => f.endsWith('.md')) : [];
  const currentTopics = Object.keys(topicIndex);
  let deletedTopics = 0;
  
  for (const file of existingTopicFiles) {
    const topic = file.replace('.md', '');
    if (!currentTopics.includes(topic)) {
      fs.unlinkSync(path.join(topicDir, file));
      deletedTopics++;
    }
  }
  
  if (deletedTags > 0 || deletedTopics > 0) {
    console.log(`✓ Deleted ${deletedTags} orphaned tag indexes, ${deletedTopics} orphaned topic indexes`);
  }
  
  // Log to MEMORY.md
  const memoryPath = '/home/julius/knowledge-base/.openclaw/MEMORY.md';
  const memoryEntry = `\n## ${today} ${new Date().toTimeString().slice(0, 8)} — Indexed\n\n- **Scanned:** ${files.filter(f => f.type === 'concept').length} concepts + ${files.filter(f => f.type === 'source').length} sources = ${files.length} total files\n- **Tags indexed:** ${Object.keys(tagIndex).length} (${allowedTags.main.length} main-tags + ${Object.keys(tagIndex).length - allowedTags.main.length} sub-tags)\n- **Topics indexed:** ${Object.keys(topicIndex).length}\n- **Orphans deleted:** ${deletedTags} tag indexes + ${deletedTopics} topic indexes\n- **Invalid tags found:** ${invalidTags.length}\n- **Errors:** ${errors.length} files skipped\n`;
  
  fs.appendFileSync(memoryPath, memoryEntry);
  console.log('✓ Logged to MEMORY.md');
  
  // Summary
  console.log('\n=== Summary ===');
  console.log(`Files scanned: ${files.length}`);
  console.log(`Tags indexed: ${Object.keys(tagIndex).length}`);
  console.log(`Topics indexed: ${Object.keys(topicIndex).length}`);
  console.log(`Orphans deleted: ${deletedTags + deletedTopics}`);
  console.log(`Invalid tags: ${invalidTags.length}`);
  console.log(`Errors: ${errors.length}`);
  
  return { success: true, tagCount: Object.keys(tagIndex).length, topicCount: Object.keys(topicIndex).length };
}

buildIndexes().then(result => {
  if (result.success) {
    console.log('\n✅ Index build completed successfully');
    process.exit(0);
  }
}).catch(err => {
  console.error('\n❌ Error:', err);
  process.exit(1);
});
