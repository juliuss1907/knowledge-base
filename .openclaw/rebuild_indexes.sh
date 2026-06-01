#!/bin/bash
cd /home/julius/knowledge-base

# Clean old indexes
rm -rf wiki/tag/*.md wiki/topic/*.md

# Create tag indexes
for tag in ai crypto tech productivity system economic politic hack tools automation vibecode research tutorial opinion; do
  mkdir -p wiki/tag
  cat > wiki/tag/${tag}.md << EOF
---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: ${tag}
auto_generated: true
last_updated: $(date +%Y-%m-%d)
---

# Tag: #${tag}

Auto-generated index of all content tagged with #${tag}.

Last updated: $(date +%Y-%m-%d %H:%M:%S)

---

*Index rebuild in progress...*
EOF
done

echo "Tag indexes created: $(ls wiki/tag/*.md 2>/dev/null | wc -l)"
