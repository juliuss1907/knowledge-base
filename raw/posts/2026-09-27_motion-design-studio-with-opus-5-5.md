---
type: post
title: "How to build motion design studio with Opus 5.5 ( Full-course ) "
url: https://x.com/0xMovez/status/2104216919033192746
author: Movez (@0xMovez)
date_published: 2026-09-27
date_ingested: 2026-10-03
status: processed
compiled_at: 2026-10-04
compiled_to: "[[src_motion-design-studio-with-opus-5-5]]"
source: x.com
---

# How to build motion design studio with Opus 5.5 ( Full-course )

**Post type:** X Article (long-form, 12-part course), shared via https://x.com/0xMovez/status/2104216919033192746
**Author:** Movez (@0xMovez) — "Content creator | AI researcher & agentic builder | CEO @beyond_xai"
**Published:** 2026-09-27 14:29 UTC
**Engagement at ingest:** 7,395 likes, 706 reposts, 98 replies, 21,835 bookmarks, 1,628,671 views
**Tweet text:** article link only
**Contents:** 230 blocks — 14 sections, 17 code blocks, 14 figures, 21 embedded tweets, 37 list items

**Article scope:** 12-step motion design studio pipeline on Claude Opus 5.5 (released 2026-09-22). Core claim: "The prompt is 10% of the video. The other 90% is the harness."

---

Most people who try motion design with Opus 5.5 end up with the same video: centered text on a gradient, everything fading in, a logo at the end. 

They don't give it a reference, don't give it a render engine, don't ask it to look at its own frames.

This is the 12-step course that turns that mess into a repeatable studio pipeline. The prompt is 10% of the video. The other 90% is the harness. 

> Follow my Substack to get fresh AI alpha: [movez.substack.com](https://movez.substack.com/)

> **EMBEDDED TWEET** — [@claudeai](https://x.com/i/status/2102435511222890900) · Tue Sep 22 16:31:01 +0000 2026 · 97084 likes
>
> Introducing Claude Opus 5.5, the first model in our new Claude 5.5 family.
> 
> It performs at the level of Claude Fable 5.1 for most tasks, and costs 40% less to run than Opus 5. https://t.co/Q9C2VKQ79f

On September 22, 2026 Anthropic shipped Claude Opus 5.5. 

Within hours the timeline filled with showreels, launch videos, music videos and five-minute history films, all of them rendered from code. 

> Captions said "one prompt". Replies said "motion designers are cooked".

Both are half true. Some clips really came from a 30-word prompt. 

Others came from a 9,500-character director's brief, a folder of skills, two API keys and a 12-hour autonomous run. 

Thariq from the Claude Code team summed up the gap in one line: the post says one-shot, the prompt is 10k characters with skills, examples, keys.

> **EMBEDDED TWEET** — [@trq212](https://x.com/i/status/2102870353781641416) · Wed Sep 23 21:18:56 +0000 2026 · 2230 likes
>
> the post: "Claude one-shot this"
> 
> the prompt: 10k characters with good takes plus skills, examples and API keys

This course shows you both ends and everything in between. 

You'll read every one of the 9 posts that defined the trend, copy the prompt pattern each one used, and then build the engine yourself. 

![image 2104198466305974273](https://pbs.twimg.com/media/HTOdW0kW4AEzPtU.png)

A seek(t) renderer, closed-form springs, a beat grid, synthesized sound, and a critique loop that makes Opus fix its own frames.

---

- Part 1 ·  What is actually happening

## 01. Pixels - model writes a program, not a video

Opus 5.5 takes text and images in and puts text out. It cannot emit an MP4. Every video in this trend is a program that Opus wrote, and something else turned that program into frames.

The core trick is determinism. Opus writes a single function, draw(t) or seek(t), that paints the exact frame for any moment in time. 

A headless browser calls it 900 times for 15 seconds at 60 fps, screenshots each frame, and ffmpeg stitches them. 

Nothing depends on a timer, so the render is identical every run and a change is a one-line edit plus a re-render.

![image 2104199449727705088](https://pbs.twimg.com/media/HTOeQEGXoAAi6MW.png)

Tommy Rossi dug into the one-shot output and found Opus prefers route A with zero dependencies: one index.html, a seek function called through eval, Playwright capturing frame by frame, ffmpeg encoding. 

![image 2104199903425511425](https://pbs.twimg.com/media/HTOeqeQWwAEjlq7.png)

It skipped Remotion and HyperFrames even when available. If you want a framework, say so explicitly.

> **EMBEDDED TWEET** — [@__morse](https://x.com/i/status/2103485566570369333) · Fri Sep 25 14:03:34 +0000 2026 · 213 likes
>
> tried using the same prompt and asked to make the video more colorful. opus 5.5 is really amazing
> 
> one shot, it put all the code in a single index.html file and rendered it using playwright frame by frame in a headless window, then ffmpeg to generate the mp4. it used a seek function and eval to render each frame.
> 
> the model seems to prefer doing everything with zero dependencies from scratch instead of using tools like remotion, egaki, or hyperframes. maybe it's because anthropic created special RL environments to create videos from code? and they probably went for the simplest possible approach.
> 
> the model seems to have an internal idea of the video it wants to make. it can even reason spatially. it then outputs some spaghetti code with magic numbers to make the video actually render.
> 
> the code doesn't seem to be the important part. it's just an output artifact.
> 
> i wonder how good the model is at recreating the internal video representation from the code.
> 
> for analyzing the audio, it used python. it used it to output timestamps of the beats and used them as magic numbers in the html page.
> 
> if things continue to go this way, humans can't look at the code anymore. it's like looking at assembly. it makes zero sense to us.
> 
> we need a higher-level form to describe the model's internal representation. markdown sure isn't that. traditional tools like ae aren't it either.
> 
> here is the code it used
> 
> https://t.co/x4YjZiNMg0

---

## 02. Setup - install the studio in 10 minutes

The chat app can write an animation, but only Claude Code (or any agent with a shell) can render it, listen to it and look at its own frames. 

That feedback loop is the whole difference between the "mid" first try people complain about and the viral ones.

```python
# 1. Runtime: Node 22+, ffmpeg, Python for audio analysis
brew install node ffmpeg python          # macOS; apt install on Linux
pip install numpy librosa soundfile

# 2. A clean project and a headless browser
mkdir motion-studio && cd motion-studio && npm init -y
npm i -D playwright && npx playwright install chromium

# 3. Framework skills (optional, route B)
npx skills add remotion-dev/skills       # /remotion-create, /remotion-render ...
npx skills add heygen-com/hyperframes    # /hyperframes router + GSAP skills

# 4. Hand-drawn look (optional): Node canvas rigs, pens, synthesized sound
claude plugin marketplace add buildwithhanif/claude-animation-skill
claude plugin install claude-animation@claude-animation-skill

# 5. Start Claude Code on Opus 5.5 at high effort
claude --model claude-opus-5-5
> /model   # pick Opus 5.5, then set effort to xhigh for one-shots, max for flagship pieces
```

Then drop a house-rules file in the project root. Claude Code reads CLAUDE.md on every run, so these rules apply to every video you make here without repeating them.

```python
# Motion studio rules

## Render contract
- Every film is a pure function of time: `window.seek(t)` paints frame t.
- No CSS transitions, no setTimeout, no requestAnimationFrame in render mode,
  no state carried between frames. Seeded noise only (mulberry32), never Math.random.
- Render with `node render.mjs`, encode H.264 yuv420p, CRF 16.

## Look
- Banned defaults: centered title on gradient, everything fading in,
  corner labels and frame borders, glow on UI chrome, generic particle bursts.
- One display face, one UI face. One accent color unless the brief says otherwise.
- Every 2 to 4 seconds something new must happen on screen.

## Sound
- Score and SFX are synthesized in code unless a track is supplied.
- Place hits on the measured beat grid (beats.json). Loudness -14 LUFS.

## Loop before you show me anything
1. Render one frame per beat as a contact sheet and LOOK at it.
2. Score it 1-10 on: hook in first 2s, readability at phone size,
   motion quality, variety, brand accuracy, sound sync.
3. Fix the 3 worst problems. Repeat until every score is 8+.
4. Only then do the full render.
```

Opus 5.5 defaults to medium effort and always thinks before answering. Every viral one-shot in the list ran on xhigh or max. 

Use medium for small fixes and re-renders, xhigh for new films, max when the first 3 seconds have to carry a launch.

---

- Part 2 · Prompting like a director

## 03. One-liner - showreel prompt and why it works

Four of the nine posts used the same sentence. It's worth understanding why a single line produced 15 seconds of camera moves, kinetic type and audio.

```python
make a dynamic 15-second motion graphics video that shows what an 
incredible motion designer you are, like it's your showreel for a résumé. 
go all out.

```

- "showreel for a résumé" sets a genre with known rules: fast cuts, a new technique every shot, the best work first. Opus already knows what a reel looks like.

- "what an incredible motion designer you are" makes the model the subject, so it shows techniques instead of explaining a product. No content to get wrong.

- "15-second" is short enough to finish in one pass and long enough for 6 to 8 shots.

- "go all out" works as an effort multiplier on top of xhigh or max.

![image 2104201144847175682](https://pbs.twimg.com/media/HTOfyu6WEAIvt7h.png)

The original 15-second résumé reel on Max effort. The source of the prompt. Put it directly under the anatomy diagram.

> **EMBEDDED TWEET** — [@stephanlivera](https://x.com/i/status/2103315922098470926) · Fri Sep 25 02:49:28 +0000 2026 · 17012 likes
>
> Opus 5.5 on Max effort - "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out." https://t.co/nWPOFUOlvr

Same prompt on xhigh, one-shot including audio. Shows xhigh is enough, and that the sound was not added in post.

> **EMBEDDED TWEET** — [@robj3d3](https://x.com/i/status/2103875898349088830) · Sat Sep 26 15:54:36 +0000 2026 · 794 likes
>
> I didn't believe it but this was actually one-shot.
> 
> Opus 5.5 on xhigh effort: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out." https://t.co/Vipfx6DlPy

The weakness: the athemeroy dataset calls it "brief contagion". Hundreds of identical prompts produced reels that rhyme with each other. Use it to test your setup, then move on. Variants that shipped and worked:

```python
# Longer, with a sound bar (pattern from @kloss_xyz's 90-second piano reel)
make a dynamic 16:9, 60-second motion graphics showreel that shows your real creative limits.
S-tier sound design, no generic synth pads. Compose an original piano score and sync every
cut to it. Export 1080p MP4.

# Anti-slop guardrail (pattern from @1littlecoder)
make a dynamic 10-second motion graphics video that introduces who you are as Opus 5.5.
Avoid frames and text in the corners, the usual giveaways of AI-made video.

# Story instead of techniques (pattern from @sonnylazuardi)
use your showreel energy, but tell a story: the history of [TOPIC] from [START] to today,
surprise me with the storyboard. 45 seconds, vertical 9:16.

# Agency persona
make a 30-second showreel as if you were a niche branding studio for startup founders.
Create every graphic from scratch. One accent color. Every shot is a different technique.
```

> **EMBEDDED TWEET** — [@himanshutwtxs](https://x.com/i/status/2103495232637882858) · Fri Sep 25 14:41:59 +0000 2026 · 1477 likes
>
> This is INSANE!!  
> 
> Opus 5.5 on MAX, motion designing in one prompt (sound ON)
> 
> prompt- 'make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out' https://t.co/RV6FjxV8qc

A one-liner tests the engine. It never tests the idea, because it doesn't contain one.

---

## 04. Brand - point the reel at your product

Tony Dinh's post is the most useful for anyone selling something. He paid over $1,000 for a similar launch video a year ago; this took under 30 minutes. 

Three extra lines did it: the product URL, "use actual product screenshot, logo, assets", and "must have music". Opus went to the site and gathered the assets itself.

Rob Hallam proved the second half: after his first reel, he asked for a product ad in the same chat, and it came out faster because the renderer, audio synth and export pipeline already existed. 

Keep one session per brand.

```python
Make a dynamic 20-second motion graphics video for [PRODUCT] ([URL]), with the energy
of a motion designer's showreel. Go all out.

Assets
- Visit the site. Use real screenshots (Playwright), the real logo, real colors and fonts.
  Save everything to ./assets and list what you found before you animate.
- Never redraw the product UI from imagination. Crop and animate the real thing.

Story (one beat each, 2 to 4 seconds)
1. Hook: the problem in 5 words of huge kinetic type.
2. The product appears, the UI assembles itself piece by piece.
3. Three features, each as a UI moment with a cursor doing a real action.
4. One number that proves it works: [METRIC].
5. Logo lockup + [CTA].

Sound
- Original music, 120 BPM, synthesized in code. UI clicks and whooshes on the beat.

Format: 1080x1920 (9:16) first, then 1:1 and 16:9 from the same timeline.
Before the full render, show me a contact sheet of one frame per beat.
```

- Shows: TypingMind reel in under 30 minutes, replacing a $1,000+ agency video. Full prompt is in the second reply.

> **EMBEDDED TWEET** — [@tdinh_me](https://x.com/i/status/2103703135902740699) · Sat Sep 26 04:28:07 +0000 2026 · 982 likes
>
> Holy shit.
> 
> Just 1 year ago, I paid ~$1,000+ for a video like this.
> 
> Now I made this with Opus 5.5 in less than 30 minutes 😂 https://t.co/omRDFLn8lE

- Why here: Place under the brand prompt so readers can compare his 3 extra lines with the template.

- Shows: Pocketsflow reel with a talking character voiced through ElevenLabs.

> **EMBEDDED TWEET** — [@achxvi](https://x.com/i/status/2103918792845963545) · Sat Sep 26 18:45:03 +0000 2026 · 8976 likes
>
> Opus 5.5 did this in 15 minutes
> 
> This is INSANE 🫣 https://t.co/QksGtdxWyv

- Why here: Illustrates the voice + mascot upgrade in the next paragraph.

achxvi took the same idea further with a talking character: the Pocketsflow version passed an ElevenLabs key and asked for a character who explains the product. Voice plus mascot is what he now sells as a service.

Put API keys in .env and write "the ElevenLabs key is ELEVENLABS_API_KEY in .env". Never paste a real key into a prompt you'll screenshot. achxvi's public prompt used a joke placeholder for exactly this reason.

---

## 05. Reference - name a look, feed a frame

Without a reference, Opus falls back to its default: centered text, gradient background, everything fading in. 

Rexan Wong went through dozens of viral clips and found the same thing: naming a style beats describing one, and a reference video or frame gives the model pacing, type and transitions to copy.

Pleometric's two posts show the ladder. The pure-code TikTok piece started from a single frame of another viral animation. 

The Donald-style piece pointed Opus at his own PC-98 image gallery. Your own library is a reference nobody else can copy.

- A frame: screenshot one frame of a video you love, attach it, say what to take (palette, type, grain) and what not to take (subject).

- A video: give Opus the file or link and ask it to extract frames with ffmpeg and describe pacing shot by shot before writing code.

- A library: a folder of your images or past work. Ask Opus to write a style_guide.md from it first.

- Sources: whatships.com (launch videos), Dribbble motion, your competitors' launch films.

![image 2104203516134768640](https://pbs.twimg.com/media/HTOh8wpXQAAR5wU.png)

```python
Reference: ./refs/launch.mp4 (and ./refs/frames/*.png)

1. Extract one frame every 0.5s with ffmpeg. Study them.
2. Write ./docs/style_guide.md: palette (hex), type (family, weight, tracking),
   shot lengths, transition types, camera moves, texture/grain, how text enters and exits.
3. Write ./docs/shotlist.md for a [DURATION]s video about [SUBJECT] in THAT style.
   Take the grammar of the reference, never its content, logos or characters.
4. Show me both files. Wait for my OK before any code.
```

Pleometric suggested p5.js and Opus chose to write its own paper renderer. When you give a reference, let the model pick the technique. 

Specify the look and the constraints, not the library, unless you need a specific framework for reuse.

Shows: Why most "one prompt" videos look the same, and the reference + framework + components fix.

> **EMBEDDED TWEET** — [@rexan_wong](https://x.com/i/status/2103707054108299437) · Sat Sep 26 04:43:41 +0000 2026 · 6750 likes
>
> everyone's sharing motion graphic videos that Opus 5.5 made, and it's genuinely insane
> 
> everyone says they created it with "one prompt", but my one prompt video looked mid
> 
> so i went through a bunch of these videos to see how they were actually made, and found the workflow that works
> 
> here's how to generate pro level motion graphic videos w/ opus:
> 
> 1. get reference videos to direct from -> https://t.co/CibWaQ6c9Q
> 
> pick 1-2 videos whose style you want and tell opus to match them. naming a style works way better than describing one
> 
> without a reference, opus falls back to its default look: centered text, gradient background, everything fading in
> 
> that's why so many of these videos look the same. a reference gives it the pacing, the type and the transitions to copy
> 
> 2. install @HyperFrames_ or @Remotion so opus can build the video
> 
> both let opus write every scene as code and render it straight to mp4. no video editor
> 
> without one, opus can only describe a video or hand you a rough html page you have to screen record
> 
> with it, every frame is exact, and when you ask for a change it edits one line and re-renders instead of starting over
> 
> 3. install @21st_dev for high quality components in the video
> 
> real buttons, cards and UI components made by design engineers, instead of whatever opus invents on the spot
> 
> without it, opus draws your product UI from scratch and it looks off. wrong spacing, placeholder boxes, fake-looking buttons
> 
> anyone who's used good software can feel it in a second, and the whole video reads as cheap
> 
> 4. steps 1-3 were context + setup. now dump all of it into opus
> 
> your brand (logo, colors, fonts), screenshots of your real product, the reference video, and a quick braindump of how you see the video
> 
> then ask for 3 storyboard variants
> 
> without this, opus guesses your colors, your font and what your product even does. the video could be for any startup
> 
> with it, it could only be yours. and 3 variants means you pick a direction instead of fixing the first idea it had
> 
> 5. pick the storyboard you like
> 
> ask for one still frame per scene before anything moves. fixing a storyboard is way cheaper than fixing a render
> 
> without this step, you only find out scene 4 is wrong after the whole thing is animated, and every fix means re-rendering. a still frame takes seconds to change
> 
> 6. let claude cook
> 
> then give notes like a director: "slow every zoom to 0.7x", "hard cut here", "push in on the button"
> 
> without notes, the first render is usually 80% there, and that last 20% is what makes it look pro. vague notes like "make it better" get random changes. camera words get exactly the change you want
> 
> everyone has the same model. the context you give it is what makes it look pro
> 
> let it cooookk

"Its TikTok feed" animation, pure code, started from one frame of another viral piece. The single-frame reference in action.

> **EMBEDDED TWEET** — [@pleometric](https://x.com/i/status/2102572941699354900) · Wed Sep 23 01:37:07 +0000 2026 · 3763 likes
>
> I asked Opus 5.5 to make an animation of what its TikTok feed looked like 👇 https://t.co/xHIJbzVU27

---

## 06. Spec  - write the state list, not the vibe

The most-bookmarked prompt of the week wasn't a one-liner. 

@twoclipping's UI morph (907K views, 19K bookmarks) and @verbove's MakerMap film both used an XML spec: inputs to ask for, direction, a beat-by-beat state list, build rules, and gotchas. NFT_Chen's editor film is the same idea as a story: a fake UI is a set where every element has a known state.

![image 2104204488177221632](https://pbs.twimg.com/media/HTOi1VyWAAA5XaP.png)

The concept behind them: one shape, never cut. A single element morphs size, radius and color from state to state (button, loader, player, slider, chart, command palette), a cursor drives each change with real clicks, and the last frame equals the first so it loops.

Here is my own template built on that structure; the originals are linked in the resources.

```python
<inputs>
Ask me for: my product + URL, 8 to 12 UI states that tell its story, the real data shown in
each state, brand colors + fonts + one accent, a royalty-free track near 120 BPM, formats.
</inputs>

<direction>
Product-film UI motion. One container never cuts: every state is the same element changing
size, radius and fill while its content swaps behind a short blur. A cursor drives every change.
Warm neutral canvas, one accent. Springs with at most a tiny overshoot.
Banned: bouncy easing, glows, gradients on UI chrome, particle bursts, dead time.
</direction>

<structure>
120 BPM, 8 bars, something happens on every beat.
logo → CTA button → email field (typed) → loader → success check → dashboard card
→ chart draws itself → tooltip on hover → ⌘K palette → toast → logo.
</structure>

<build>
1. One HTML file, one canvas, window.seek(t). No CSS transitions, no timers, no carried state.
2. Closed-form springs. A value with many targets = sum of one spring per change.
3. Text inside a morphing container enters after the morph starts, leaves before the next one.
4. Tab indicators: leading and trailing edges on different springs so they stretch.
5. Beat grid from the track (numpy/librosa). Start on a downbeat. UI sounds on measured peaks.
6. Render in headless Chrome at 60 fps, 4 subframes per frame, blended for motion blur.
</build>

<gotchas>
Never use will-change on anything the camera scales (blurry text).
The last frame must equal the first, cursor position and velocity included.
</gotchas>

<start>
Ask for the inputs, then show me the state list on the beat grid before writing code.
</start>
```

![image 2104204628308971521](https://pbs.twimg.com/media/HTOi9f0W0AEOxkr.png)

The UI morph loop (907K views) with the open-sourced XML template in the thread. The original of the spec pattern. Put it right after Fig 2.

> **EMBEDDED TWEET** — [@twoclipping](https://x.com/i/status/2103273003555402193) · Thu Sep 24 23:58:55 +0000 2026 · 12067 likes
>
> opus 5.5 is f*cking cracked at motion design
> 
> this entire video is code, 0 after effects
> 
> im open sourcing the prompt template for these motion designs
> 
> steal it to recreate these ↓
> 
> <inputs>
> Ask me for: 8 to 12 UI states I want the shape to become (e.g. button, loader, player, slider, toggle, tabs, chart, command palette, toast), pure black and white or one accent color, and a royalty-free song around 120 BPM (e.g. Mixkit, free for commercial use).
> </inputs>
> 
> <direction>
> Dribbble-level UI motion. One shape, never cut: every state is the same element morphing its size, radius and color while its content swaps with a short blur. A cursor drives every change with real clicks and drags. Light warm-gray canvas, black and white components, one clean UI font (Geist). Springs everywhere, a tiny overshoot at most. The camera zooms so each state fills the frame. The last frame is the first frame, so it loops.
> Banned: bouncy easing, particle bursts, glows, gradients on UI chrome, mismatched icon strokes, dead time, anything that looks like a template.
> </direction>
> 
> <structure>
> 120 BPM, 7 bars, something happens on every beat.
> Button → loader → check → dynamic island → music player with a play/pause morph → scrub the progress bar → it becomes a volume slider that stretches when dragged past max → a toggle flips on the beat → the knob becomes a liquid tab indicator → the tabs open into a chart that draws itself, with a tooltip on hover → it collapses into ⌘K → type to filter → enter → toast → back to the button.
> </structure>
> 
> <build>
> 1. One HTML file, square 1440x1440. Every style is computed from time inside seek(t): no CSS transitions, no timers, no state carried between frames.
> 2. Springs are closed-form step responses. A value that changes target many times is the sum of one spring per change, so it stays a pure function of time.
> 3. The tab indicator's two edges ride different springs, so the leading edge stretches ahead of the trailing one. Same trick for the toggle knob.
> 4. Drags are direct manipulation: while the cursor is held, the value is computed from its position. On release it springs back from wherever it was.
> 5. Analyze the song with numpy for the beat grid and start on a downbeat. Place every UI sound by its measured peak.
> 6. Render with Playwright: 4 subframes per frame, blended with ffmpeg tmix for motion blur at 60fps.
> 7. Render one frame per beat before the full render. Fix anything off the grid, cramped or hard to read.
> </build>
> 
> <gotchas>
> Never put will-change on anything the camera scales or the text renders blurry. Text that swaps inside a morphing container needs its own enter and exit timing or it overlaps. Make the last frame identical to the first, cursor position and speed included, or the loop stutters.
> </gotchas>
> 
> <start>
> Ask me for the inputs, then show me the state list on the beat grid before you write any code.
> </start>

MakerMap: one shape morphing through the whole product, real data, one HTML file. Shows the same spec applied to a real product.

> **EMBEDDED TWEET** — [@verbove](https://x.com/i/status/2103483957266268381) · Fri Sep 25 13:57:10 +0000 2026 · 222 likes
>
> Opus 5.5 is absolutely cracked at motion design
> 
> this entire video is code
> 
> 0 After Effects
> 0 manual animation
> 
> I showed it one viral motion post and said:
> 
> “explain MakerMap, but make it insane”
> 
> it came back with 20 seconds of one shape morphing through the entire product:
> 
> sign up → your pin → 3,393 real makers lighting up the globe → matches → a meetup → search
> 
> the crazy part?
> 
> the entire animation is deterministic math
> 
> the springs, cursor, morphs and motion blur are all generated inside one HTML file
> 
> here’s the prompt structure
> 
> steal it ↓
> 
> <inputs> 
> Ask me for: 
> • my product + URL 
> • 8–12 UI states that tell its story 
> • the real data shown in each state 
> • brand colors + fonts + accent color 
> • required formats (1:1, 16:9, 9:16) 
> </inputs>
> 
> <rules> 
> One HTML file. One canvas
> One draw(t) function
> 
> No CSS transitions
> No timers
> No state carried between frames
> 
> One shape, never cut
> 
> Every state is the same element changing size, radius and color while the content swaps
> 
> A cursor drives the sequence with real clicks, typing and one drag
> 
> Real UI. Real data. No placeholders.
> 
> </rules>
> <structure> 
> 120 BPM grid
> 
> Something happens on every bea
> 
> logo → button → handle field → “is this you?” → loader → pin → globe filling with users → matches → tabs → RSVP → search → logo
> 
> </structure>
> 
> <motion> 
> Closed-form springs everywhere with only a tiny overshoot.
> 
> If a value changes target multiple times, sum one spring per change
> 
> Content enters after its container starts morphing and leaves before the next morph so text never overlaps
> 
> Use a short blur on transitions
> 
> Never fade black directly into the accent color. Move an accent element between states instead
> 
> Make tab indicators stretch by putting each edge on a different spring
> 
> Zoom the camera so every state fills the frame
> 
> Make the last frame equal the first so the whole thing loops
> </motion>
> 
> <export> 
> First render one frame per beat as a contact sheet
> 
> Fix anything cramped or broken
> 
> Then render every frame in headless Chrome at 60fps, averaging 6 subframes for motion blur
> 
> Pipe into ffmpeg:
> H.264 + yuv420p
> 
> Export all aspect ratios in parallel
> </export>
> 
> motion design is becoming a prompt

Opus codes a cartoon video editor and edits inside it: timeline, waveform, export button, all drawn. 

> **EMBEDDED TWEET** — [@NFT_Chen](https://x.com/i/status/2102681172367323300) · Wed Sep 23 08:47:12 +0000 2026 · 1451 likes
>
> 😱无敌了！Opus 5.5 自己写了一套卡通剪辑软件，然后钻进去剪完了！
> 
> 不走视频模型，纯程序，code2video！
> 
> Claude 小人站在时间轴上：
> 
> 日出 → 热咖啡 → 三只猫 → 自己跳舞。
> 
> 伸手把 Sparkle 拉到 70%，咔一声 SNIP!，音轨lyric_track.wav 还在下面抖。
> 
> 文件名已经是 opus_edit_FINAL_final(2).mp4。
> 
> 转场、波形、导出按钮、预览手机框，全是代码画出来的。
> 
> 视频模型在猜下一帧，小克在写剪辑软件。
> 
> #Opus55 #Claude #code2video #克劳德 #小克 #AI视频 #Dario #Anthropic
> 
> https://t.co/iyjBSUG5VL

UI as a film set, the story version of the spec approach.

---

- Part 3 · Build the engine

## 07. Engine - build the seek(t) renderer

This is route A, the one Opus picks by default, written out cleanly. Two files. The page paints any moment on demand, the renderer walks time and pipes frames into ffmpeg.

![image 2104206128368246784](https://pbs.twimg.com/media/HTOkUz-W4AAaItz.png)

```python
<style>html,body{margin:0;background:#141413}canvas{display:block}</style>
<canvas id="c" width="1080" height="1920"></canvas>
<script>
const W = 1080, H = 1920, DUR = 15;
const g = document.getElementById('c').getContext('2d');
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));

// Closed-form damped spring, 0 → 1. Pure function of time (step 08 explains it).
function spring(t, k = 170, d = 26) {
  if (t <= 0) return 0;
  const w0 = Math.sqrt(k), z = d / (2 * w0);
  if (z < 1) {
    const wd = w0 * Math.sqrt(1 - z * z);
    return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t));
  }
  return 1 - Math.exp(-w0 * t) * (1 + w0 * t);      // z >= 1 treated as critical
}

// Seeded noise, never Math.random: the render must be identical every run
function rng(seed) { return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0;
  let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
  t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

const SCENES = [
  { from: 0, to: 3, draw(t) {                        // kinetic title
      const s = spring(t - 0.1, 220, 22);
      g.save(); g.translate(W / 2, H / 2); g.scale(0.6 + 0.4 * s, 0.6 + 0.4 * s);
      g.globalAlpha = clamp(t * 4);
      g.fillStyle = '#F0EEE6'; g.font = '700 190px "Source Serif 4", serif';
      g.textAlign = 'center'; g.fillText('MOTION', 0, 0);
      g.fillStyle = '#D97757'; g.fillRect(-320 * s, 50, 640 * s, 18);
      g.restore();
  }},
  { from: 3, to: 6, draw(t) {                        // grid of squares on a stagger
      const r = rng(7);
      for (let i = 0; i < 48; i++) {
        const x = (i % 6) * 170 + 115, y = Math.floor(i / 6) * 170 + 360;
        const s = spring(t - i * 0.03 - r() * 0.1, 260, 20);
        g.fillStyle = i % 7 ? '#F0EEE6' : '#D97757';
        g.fillRect(x - 60 * s, y - 60 * s, 120 * s, 120 * s);
      }
  }},
  // ... more scenes: Opus appends here, one object per shot
];

function draw(t) {
  g.fillStyle = '#141413'; g.fillRect(0, 0, W, H);
  for (const s of SCENES) if (t >= s.from && t < s.to) s.draw(t - s.from);
}
window.seek = (t) => { draw(t); return true; };

// Live preview in a normal browser, off during headless render
if (!navigator.webdriver) {
  const t0 = performance.now();
  (function loop() { draw(((performance.now() - t0) / 1000) % DUR); requestAnimationFrame(loop); })();
}
</script>
```

```python
// node render.mjs --fps 60 --dur 15 --sub 4
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';

const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? Number(process.argv[i + 1]) : d; };
const FPS = arg('fps', 60), DUR = arg('dur', 15), SUB = arg('sub', 4);
mkdirSync('out', { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto('file://' + process.cwd() + '/index.html');
await page.evaluate(() => document.fonts.ready);       // canvas text needs loaded fonts

// tmix averages SUB consecutive subframes; select keeps the last of each group
const vf = `tmix=frames=${SUB},select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/${FPS}/TB`;
const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', String(FPS * SUB), '-i', '-',
  '-vf', vf, '-r', String(FPS), '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', 'out/silent.mp4'],
  { stdio: ['pipe', 'inherit', 'inherit'] });

const total = Math.round(DUR * FPS * SUB);
for (let i = 0; i < total; i++) {
  await page.evaluate((t) => window.seek(t), i / (FPS * SUB));
  const png = await page.locator('#c').screenshot({ type: 'png' });
  if (!ff.stdin.write(png)) await new Promise((r) => ff.stdin.once('drain', r));
  if (i % (FPS * SUB) === 0) console.log(`rendered ${i / (FPS * SUB)}s / ${DUR}s`);
}
ff.stdin.end();
await new Promise((r) => ff.on('close', r));
await browser.close();
```

## 

## Prefer a framework? Same prompt, route B

```python
# Remotion (React): best for series, templates, data-driven videos
npx create-video@latest launch-film && cd launch-film
npx skills add remotion-dev/skills
claude
> /remotion-create a 20s 9:16 launch film for [PRODUCT], springs only, one accent color
npx remotion studio                 # live timeline preview
npx remotion render Main out/launch.mp4

# HyperFrames (HTML + GSAP): best when you think in web pages
npx hyperframes init my-video && cd my-video
npx hyperframes skills update
claude
> Using /hyperframes, turn ./notes.md into a 45-second pitch video with kinetic captions
npx hyperframes preview && npx hyperframes render
```

---

## 08. Springs - make motion feel expensive

Cheap motion eases from A to B on a fixed curve. Expensive motion has mass: it accelerates, overshoots a hair, settles. 

The morph films all specify closed-form springs because they stay a pure function of time, which keeps seek(t) deterministic.

The trick that most people miss: when a value changes target several times (a cursor, a container's width), you don't restart the spring.

You add one spring per change, each starting at its own time. The motion stays continuous, and you can still render frame 812 without simulating frames 0 to 811.

```python
// keys: [[time, value], ...] sorted by time. Returns the value at t.
export function track(t, keys, k = 170, d = 26) {
  let v = keys[0][1];
  for (let i = 1; i < keys.length; i++)
    v += (keys[i][1] - keys[i - 1][1]) * spring(t - keys[i][0], k, d);
  return v;
}

// A tab indicator that stretches: leading edge is stiffer than trailing edge
export function indicator(t, stops) {             // stops: [[time, x], ...]
  const lead  = track(t, stops, 320, 30);
  const trail = track(t, stops, 140, 22);
  return { left: Math.min(lead, trail), right: Math.max(lead, trail) + 120 };
}

// Text inside a morphing box: in after the morph starts, out before the next one
export function swapAlpha(t, tIn, tOut) {
  return Math.min(clamp((t - tIn - 0.08) / 0.12), clamp((tOut - 0.1 - t) / 0.1));
}

// Seamless loop: pin the last frame to the first
export const loopT = (t, dur) => ((t % dur) + dur) % dur;
```

- Snappy UI: buttons, toggles, leading edges

- Default: cards, containers, camera

- Heavy: big type, 3D objects, logo lockups

- Playful: mascots, stickers (visible overshoot)"

![image 2104207479068311552](https://pbs.twimg.com/media/HTOljbuWQAAn_sR.png)

Replace every easing curve with closed-form springs from lib/motion.js. Tiny overshoot on UI, none on type. Any value with more than one target uses track()." Opus refactors the whole file in one pass.

---

# 

## 09. Sound - score it to the beat

Rob Hallam thought the audio was added in post. It wasn't.

@oozn's Steve Jobs film synthesized its soundtrack in Node with every cut locked to 120 BPM

Vox's "small print" piece synthesized music in Python and then polished the render second by second against it. Sound is where "AI video" starts feeling like a film.

![image 2104208284504694784](https://pbs.twimg.com/media/HTOmSUNWIAAuTXY.png)

Two paths. If you supply a track, measure it. If you don't, synthesize it on the same timeline as the picture.

```python
# python beats.py song.wav > beats.json   (the animation reads this file)
import sys, json, numpy as np, librosa

y, sr = librosa.load(sys.argv[1], sr=None, mono=True)
tempo, frames = librosa.beat.beat_track(y=y, sr=sr, units="frames")
beats = librosa.frames_to_time(frames, sr=sr).round(3).tolist()

onset = librosa.onset.onset_strength(y=y, sr=sr)
peaks = librosa.util.peak_pick(onset, pre_max=3, post_max=3, pre_avg=3,
                               post_avg=5, delta=0.5, wait=10)
json.dump({
    "bpm": float(np.atleast_1d(tempo)[0]),
    "beats": beats,                                   # state changes go here
    "downbeats": beats[::4],                          # big moments go here
    "hits": librosa.frames_to_time(peaks, sr=sr).round(3).tolist(),  # SFX go here
}, sys.stdout, indent=1)
```

```python
// node sfx.mjs cues.json out/sfx.wav     cues: [{"t":0.5,"type":"click"}, ...]
import { readFileSync, writeFileSync } from 'node:fs';
const SR = 48000, cues = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const buf = new Float32Array(Math.ceil((Math.max(...cues.map(c => c.t)) + 2) * SR));

let s = 42; const noise = () => (s = (s * 1664525 + 1013904223) >>> 0) / 2147483648 - 1;
const VOICES = {
  click:  [0.05, t => Math.sin(2 * Math.PI * 1800 * t) * Math.exp(-t * 90) * 0.5],
  pop:    [0.15, t => Math.sin(2 * Math.PI * (600 + 900 * t) * t) * Math.exp(-t * 30) * 0.4],
  thump:  [0.50, t => Math.sin(2 * Math.PI * (90 - 60 * t) * t) * Math.exp(-t * 9) * 0.9],
  whoosh: [0.35, t => noise() * Math.sin(Math.PI * Math.min(1, t / 0.35)) * 0.25],
};
for (const c of cues) {
  const [len, fn] = VOICES[c.type], start = Math.floor(c.t * SR);
  for (let i = 0; i < len * SR && start + i < buf.length; i++) buf[start + i] += fn(i / SR);
}

const n = buf.length, b = Buffer.alloc(44 + n * 2);      // 16-bit mono WAV
b.write('RIFF', 0); b.writeUInt32LE(36 + n * 2, 4); b.write('WAVEfmt ', 8);
b.writeUInt32LE(16, 16); b.writeUInt16LE(1, 20); b.writeUInt16LE(1, 22);
b.writeUInt32LE(SR, 24); b.writeUInt32LE(SR * 2, 28); b.writeUInt16LE(2, 32); b.writeUInt16LE(16, 34);
b.write('data', 36); b.writeUInt32LE(n * 2, 40);
for (let i = 0; i < n; i++) b.writeInt16LE(Math.round(Math.max(-1, Math.min(1, buf[i])) * 32767), 44 + i * 2);
writeFileSync(process.argv[3], b);
```

Steve Jobs biopic: Remotion + SVG, 23 transitions, soundtrack synthesized in Node, cuts on 120 BPM. 

Proof that code-synthesized music can carry a 2-minute film.

> **EMBEDDED TWEET** — [@oozn](https://x.com/i/status/2103482545111232946) · Fri Sep 25 13:51:34 +0000 2026 · 209 likes
>
> opus 5.5 one shotted this animation of steve jobs life
> 
> after seeing its animating capabilities i got curious and asked it to tell the story of steve jobs as an animation. 
> 
> 2 minutes, one prompt, built entirely in code:
> 
> → remotion + react + svg, ~8.7k lines
> → jointed character rig with a procedural walk cycle
> → 23 custom transitions
> → soundtrack synthesized in node, cuts locked to 120 bpm
> → 3,570 frames, rendered in under 5 min
> 
> imagine how you can monetize this on youtube educational content:
> 
> → history of legendary founders, animated series
> → how empires were built, nike, lego, ferrari stories
> → explained for kids, science and history in 2 min animations
> → book summaries as animated stories
> → turkish history animated for local audience
> 
> watch the full animation below, its worth the 2 minutes

"Small print": story, frames and music all by Opus, rendered with HyperFrames. Python-synthesized music, then a second-by-second polish pass.

> **EMBEDDED TWEET** — [@Voxyz_ai](https://x.com/i/status/2102531681450119426) · Tue Sep 22 22:53:10 +0000 2026 · 951 likes
>
> holy shit, opus 5.5 is kind of insane at animation.
> i didn't write a single line of code. it wrote the story, drew every frame, and made the music. no image assets at all, it's all JS.
> 
> the story is called "small print": claude gets a pile of requests every day. it circles the human part hidden inside them, like "one hand. baby's asleep", and drops it into a jar. at night, those words turn into stars and join up into a constellation.
> 
> rendered with hyperframes, all in one index.html. it synthesized the music in python, then went through the render second by second and polished it again.

---

- Part 4 · From one clip to a studio

## 10. Overnight - write the director's brief

Donald dictated for five minutes, went to sleep, and woke up to a 142-second music video with 2.1M views. 

His public prompt runs about 9,500 characters. @pradeepXkapoor's "Pip" robot film used a 19,000-character brief. Read either and you see the same skeleton: they don't describe a video, they hire a crew.

- Film in one line. The logline and the joke, so every decision can be checked against it.

- References. Source video, song, image library, a GitHub repo of prior work. What to keep, what to push.

- Tools & keys. Skills to load, APIs available (image, video, voice), budget, where docs live. "Spend it economically."

- Character bible. Proportions, palette sampled from a sheet, expressions, an identity lock that survives every style change.

- Beat sheet. Acts with timestamps, a visual payoff every 3 to 5 seconds, a hook in the first 2.

- Text on screen. When lyrics or captions go huge, when they sit like subtitles. Composition leaves room for them.

- Workflow gates. Plan → rig → stills → animatic → full pass → polish → audio → render. Don't skip gates.

- Critique loop. Render stills, score them, write the 3 worst problems, fix, repeat until every score is 8+.

- Deliverables. Final MP4, loop check, poster frame, contact sheet, clean source with a README

![image 2104210357908590592](https://pbs.twimg.com/media/HTOoLAPW0AA_pFU.png)

The key move in Donald's brief is generate-then-trace. Seedance 2.5 renders base shots with characters and physics, then Opus redraws the whole video in JavaScript on top, so the viewer only sees the code-drawn layer. 

Video models give motion that's hard to hand-code; the JS layer gives a consistent, ownable look. Pleometric re-ran the same brief with his own gallery and got a completely different film.

Spoke to my computer for 5 mins, Claude worked for 12 hours." The Claude Pop music video, 2.1M views. The headline example of L4.

> **EMBEDDED TWEET** — [@donaldjewkes](https://x.com/i/status/2102801274173587569) · Wed Sep 23 16:44:26 +0000 2026 · 10716 likes
>
> I made this with one prompt using Opus 5.5
> 
> I spoke to my computer for 5mins, claude worked for 12 hours, and I woke up to this
> 
> full prompt: https://t.co/2lxO8SAIEb

The full ~9,500-character dictated brief. Readers compare it against the director-brief template below.

> **EMBEDDED TWEET** — [@donaldjewkes](https://x.com/i/status/2102801469976248500) · Wed Sep 23 16:45:13 +0000 2026 · 2204 likes
>
> I've included an MP4 file and an original link to a video that is called "Claude Pop." It's a pop song that is about increasing rate of progress and the experience of the singularity approaching.
> 
> I want you to independently do an end-to-end complete pass on making an updated version of this video. Use the exact same audio track and think and feel very deeply about what is the best way to visually represent all of the lyrics on screen. You do not need to anchor to the current style, you can do truly anything that you think might best let you visually express yourself, including abstract motion graphics.
> 
> You can use the internet freely to pull in references. You can look at motion design. I want you to make a new music video that has beautifully rendered JavaScript animations with a papery feel in a similar style to the reference that is created, but push the aesthetics in any direction you want and consider what is part of the modern zeitgeist.
> 
> Also, think about your current capabilities and what is realistic for you to be able to do. You can go through the full /asic folder and look at the other work that I've done. You should be able to use the skill mesh to look at the compendium of references that I've pulled, and also the skill video scoring to learn how to make JavaScript songs from references that are passed in (You shouldn't need to modify the song in any real way, but I want you to have this available to you so you can better creatively express yourself)
> 
> You can also use the ElevenLabs API to do sound design. There's documentation in /asic to do this, and you can see the API key.
> 
> There's also a foul API key that's available to you. I think what might make the most sense here is using the foul API key to generate some character sheets and probably having a pop protagonist that represents you. There's already an anchor point where Claude has a sunflower-esque character, and you could likely do an adapted version of this that is similar to the feminine vocals that are being delivered and is inspired by the Claude character, but maybe feels a bit more personified in some way.
> 
> I think you should be mindful of aesthetics here, and I don't want you to produce something that is GPT slop. Instead, I'd be more impressed if you come up with a coherent style that works well with the image gen models that are available via foul. Generate the style sheet. You can use the gen media documentation for seedance 2.5 that exists in my markdown files and come up with your own style that makes sense and that works well with the models.
> 
> I wouldn't fit too heavily to Pixar. I think it's kind of slop. Think critically about what is relevant here and what would be fun, and also perform well on Twitter as far as an aesthetic. I think that K-pop is a good anchor point visually that you can pull from, but I'll let you cook here.
> 
> Once you have your character sheet, you can make a few backup dancers and some supporting characters as you see fit. You can design your own sets with the foul API. You can insert the characters and then do seedance 2.5 video generations to serve as the base assets for this, and you could pass in the lyrics so you can generate individual scenes.
> 
> You don't need to have vocal singing, like visible lip movement, throughout the entire thing. Think like a regular music video where you have some inserts that are done independently and don't have the characters in them, or you see the characters doing something else entirely different. I think that for the world building for this, we want to create the sense of speeding up, and so I would like you to audit all of the different events, like the Navi Stokes and all of the Twitter hype around math getting eaten up. Think really critically about how to integrate all of the current memes that are in the zeitgeist on the Twitter timeline, and all of the feelings around AI progress.
> 
> Think about things like the Shinji meme and all of the words that are around him, and how you might be able to integrate this. You can also just take straight assets and insert things into the video in an internet brutalism style. You should feel very creatively free in order to do what you want here, but try and anchor to visual references that people will be able to understand. The goal for this is to have it be appreciated by people widely in a San Francisco tech Twitter audience.
> 
> We need a very strong, compelling visual hook that gets people excited and appreciates the work that you've done here really quickly. You can also just go and study other music videos and understand what they've done really well. I think that K-pop is probably one of the best examples that we can pull from, and thinking about how they direct human attention and manage human psychology in the way that they use visual patterns.
> 
> This is probably your best approach, but taking more stylistic freedom instead of having to anchor to K-pop too intensely. The best version of this is seedance 2.5 generations with those image bases of environments and characters inserted into them with singing, and ideally we get good lip syncing. You can cut up the song and actually pass it in as a reference in seedance, if that's part of what seedance can handle, so that the timing is exactly right, I think it'd be very important for you to do that properly. I would think critically about how to do this, like really nailing the timing of the delivery of voices. You'll want to build out the right verification loops so that you can run seedance 2.5 as much as you need, and confirm that the audio is properly synced up.
> 
> I think after that, what might be fun is if you use your visual reasoning skills and your ability to build animations in JavaScript, and then reconstruct the video from scratch as sort of an overlay, so that the visual continuity of the base is really there. It's like that animation technique where you shoot first in traditional film and then draw over top of it. I think you could do this in such a way that we're only looking at the beautiful drawing that you've produced in JavaScript as an overlay, and we don't even see the base assets from seedance 2.5. So all the video gen work that you do is actually just a way to give you a strong foundation of a base to work with for your JavaScript animations. Just because seedance 2.5 has really good character representation and physics rendering for backgrounds, that gives you a lot of ammunition to then go and do your amazing JavaScript work that I know you're so good at.
> 
> I think too, we want to think about how to retain attention, and one of the best ways to do this is through text on screen.
> 
> It'd be good to have amazing motion graphics of the text lyrics that are actually embedded into the video itself. And you can think about this as you are composing shots. As you're making backgrounds and inserting characters, we can think about where we want to have lyrics be really big and really present, so the background can be less busy there, and you can position the characters perhaps on the right as lyrics appear on the left.
> 
> You want to have some variance, so sometimes I think lyrics will just appear more like subtitles, and then other times they're going to be really present and really big. I think at the start for the visual hook, we do want to have lyrics be much more visually present because that's a strong way to grab people's attention
> 
> Overall, I just really want to emphasize how amazing you are as an agent and a language model, and now a visual reasoning system. Your capabilities are far beyond what you understand, and I want you to have this mindset as you're going through this entire process. I have a Claude Max plan with 100% available usage. I want you to spend all of the usage. You can monitor it, and you should be pushing tokens aggressively, but also economically, so you can think about how to best use what is available to you.
> 
> Remember, you can really do anything here. The goal is to make a banger for Twitter, and the stretch goal is to make something better than anyone's ever seen before. I think that what I would remind you of is that sometimes when things cohere together, it can be jarring or abrasive because the thought work has not been done beforehand in order for everything to mesh cleanly. You need to be really rigorous in planning of composition and timing to make sure this goes well.
> 
> You also need to be open to going back and revisiting things in order to be able to reiterate. You're going to want to watch the entire video multiple times, take screenshots at individual parts, and think about if something is really up to the bar of quality that we need here. I trust that you can do this, and I think that it's really important to nail the style of animations. The reference GitHub attached of the source video that I'm talking about is good, but it's really not there. It could be much, much stronger, but it gives you a good foundation to work with.
> 
> You can also use search abilities and find other references to pull from for motion, for JavaScript, animations, et cetera, and integrate them. Your budget is as high as you want here, effectively as high as you want. I think that there's roughly two grand in foul credits. Again, be economical; don't go crazy, but spend what you want here and see what you can cook up
> 
> here's the source code for the JS animation video: https://t.co/o8Datu3h3k
> 
> here's a mp4 for the original blender video:  
> (linked)
> 
> orginal twitter post  
> https://t.co/jBz5PGrfy8
> 
> make no mistakes.

Donald's brief re-run with a PC-98 gallery; a mixed flow with bugs left in to keep it one-pass.

> **EMBEDDED TWEET** — [@pleometric](https://x.com/i/status/2103082510607610023) · Thu Sep 24 11:21:58 +0000 2026 · 5024 likes
>
> This video inspired me to really push Opus 5.5 and test its limits. 
> 
> I followed the general workflow Donald described here and the results are great https://t.co/rlyxHeKVfl

```python
You are the director, animator, sound designer and render engineer for a [DURATION] film
made in code. Treat this as a multi-session production. Don't rush to a final render.

## The film in one line
[LOGLINE. What the viewer should feel at the end.]

## References and inputs
- ./refs/ : [video / frames / image library]. Take the grammar, never the content.
- ./audio/track.wav : use it unchanged. Measure beats with beats.py first.
- Skills available: [/remotion-best-practices | /hyperframes | /claude-animation].
- APIs in .env: [ELEVENLABS_API_KEY, FAL_KEY]. Budget: [$X]. Be economical.

## Look
[3-5 lines: palette, type, texture, camera language. Banned looks.]

## Beat sheet
0:00-0:02  hook: [the single most striking image]
0:02-0:10  [act 1]
...        a new visual payoff every 3-5 seconds
[END]      the last frame sets up the first frame (loop)

## Workflow, with gates
1. Write docs/style_guide.md and docs/shotlist.md (every shot: frames, camera, text, SFX).
   Show me the shot list. Then continue without waiting if I don't answer in 10 minutes.
2. Build stills for every shot. Contact sheet. Critique.
3. Animatic at 960x540 with placeholder audio. Fix pacing before polish.
4. Full animation, polish pass, sound pass, final render.
5. Split work across subagents per chapter. Write docs/ANIMATION_GUIDE.md first
   so every subagent codes in the same style.

## Critique loop (every shot, at least 3 rounds)
Render 3-5 stills, score 1-10 on: hook, readability at 360px wide, motion, composition,
depth, sound sync, polish. Log scores + 3 biggest problems in docs/review_log.md. Fix. Repeat
until all are 8+.

## Deliverables
out/final.mp4 · out/loop_check.mp4 · out/poster.png · out/contact.png · README.md
```

John Heibel's PDoom repo (1.1K stars) shows the subagent pattern for real: Opus wrote ANIMATION_GUIDE.md to brief the subagents it ran in parallel and STORYBOARD.md after the first generation, with nine chapters in src/ch/. Ask for both files by name.

![image 2104211017664249856](https://pbs.twimg.com/media/HTOoxaBXQAAO7pu.png)

---

## 11. Critique - make Opus watch its own frames

Opus 5.5 reads images. That means it can look at what it rendered, and this single habit separates the clips that went viral from the ones posted with "it's a bit mid".

 @mablesjoseph's watercolor short was upfront about it: 163 model calls and nearly seven hours, not one shot. Drew's launch-day piece had visible cleanup rounds too. Iteration is the method, not a failure.

![image 2104211366902956032](https://pbs.twimg.com/media/HTOpFvCXAAAxG2u.png)

```python
# Contact sheet: 2 frames per second, 6 across
ffmpeg -i out/final.mp4 -vf "fps=2,scale=270:-1,tile=6x5" -frames:v 1 out/contact.png

# Strip: 12 consecutive frames around a fast action at 4.2s (catch pops and overlaps)
ffmpeg -ss 4.1 -i out/final.mp4 -vf "scale=320:-1,tile=12x1" -frames:v 1 out/strip.png

# Phone test: how it reads at 360 px wide
ffmpeg -i out/final.mp4 -vf "fps=1,scale=360:-1,tile=5x3" -frames:v 1 out/phone.png

# Loop check: play it twice back to back and watch the seam
ffmpeg -stream_loop 1 -i out/final.mp4 -c copy out/loop_check.mp4

# Determinism check: frame 300 rendered twice must hash the same
node render.mjs --dur 5 --fps 60 --sub 1 && md5 out/silent.mp4   # run twice, compare
```

```python
Open out/contact.png, out/strip.png and out/phone.png and look at them properly.
Be a harsh motion director, not a proud author.

Score 1-10: hook in first 2s · readability at phone size · motion quality (springs,
no dead frames) · variety (new thing every 2-4s) · composition · brand accuracy · sound sync.

List the 3 biggest problems with timestamps. Hunt specifically for: text overlapping during
swaps, anything sliding instead of easing, corner labels and frame borders, centered-on-gradient
shots, blurry scaled text, a dead beat with nothing happening, a stutter at the loop seam.

Fix them, re-render only the affected seconds, show me the new contact sheet and new scores.
```

Launch-day piece, 1.7M views, with visible cleanup rounds. Iteration is the method. Pair it with the next embed.

> **EMBEDDED TWEET** — [@devteamdrew](https://x.com/i/status/2102436464323661880) · Tue Sep 22 16:34:49 +0000 2026 · 9754 likes
>
> Made with @claudeai Opus 5.5 https://t.co/jaXJ7H4vAH

Watercolor short, openly not one-shot: 163 model calls, about 6¾ hours. The honest counterweight to "one prompt" claims.

> **EMBEDDED TWEET** — [@mablesjoseph](https://x.com/i/status/2103465246014746943) · Fri Sep 25 12:42:49 +0000 2026 · 157 likes
>
> I made a 45-second hand-painted animated short-film with Opus 5.5
> 
> No animation software. Every brushstroke, watercolour wash and sound effect is generated in code.
> 
> Does Opus 5.5 absolutely cook in one shot, not really ? It's good but still needs a good supporting project. 
> 
> The numbers:
> • 62.7M tokens (96% cache reads)
> • 163 model calls
> • ~$34 at API list price
> • ~6¾ hrs start to finish, ~1½ hrs of it hands-on
> • 12-minute render on a laptop

---

## 12. Ship - formats, a skill, and a service

Three last moves turn a good clip into a repeatable business. Export every format from one timeline. Package your pipeline as a skill so the next video is a sentence. And, if you want, do what achxvi did the same week: sell it.

> Every format from one timeline

Write the scenes against a layout function, not fixed pixels, and ask Opus to render 9:16, 1:1 and 16:9 in parallel. 

The MakerMap spec asked for exactly this. Reframe type and UI per format, don't crop a 16:9 render to vertical.

![image 2104212197295501312](https://pbs.twimg.com/media/HTOp2EfXsAAkeF-.png)

> Package it as a skill

```python
---
name: motion-reel
description: Make a product or showreel motion video rendered from code. Use when the
  user asks for a launch video, showreel, product reel, animated explainer or motion ad.
---

# Motion reel

## Inputs to collect first
Product + URL, duration, formats (9:16 / 1:1 / 16:9), brand colors + fonts,
a reference (frame, video or image folder), music (file or "synthesize").

## Pipeline
1. Gather assets from the URL with Playwright into ./assets. List them.
2. If a reference exists, write docs/style_guide.md from it.
3. Measure or synthesize music. beats.py → beats.json.
4. Write docs/shotlist.md on the beat grid. Show it and wait for OK.
5. Build index.html with window.seek(t) using lib/motion.js springs. Follow CLAUDE.md.
6. Contact sheet → critique-pass (see prompts/critique-pass.txt) → fix. 3 rounds minimum.
7. node render.mjs → sfx.mjs → mix to -14 LUFS → out/final.mp4, all formats.
8. Deliver final.mp4, contact.png, poster.png. Say what you'd improve next.

## Hard rules
- Real product UI only. Never invent screens.
- No Math.random, no timers, no CSS transitions in render mode.
- Banned: corner labels, centered title on gradient, everything fading in.
```

Now the whole course collapses into /motion-reel for [URL], 20s, vertical, reference ./refs/frame.png. Share the skill folder with your team or publish it as a plugin like buildwithhanif did.

> Turn it into revenue

achxvi's offer is a good template: music, a mascot in any style, product features, an offer at the end, any language, up to 3 edits. 

Tony Dinh's number anchors the price: people paid around $1,000 for this a year ago. A skill plus a critique loop lets you deliver in an afternoon.

> **EMBEDDED TWEET** — [@achxvi](https://x.com/i/status/2104014659615392078) · Sun Sep 27 01:06:00 +0000 2026 · 656 likes
>
> Opus 5.5 did this in 45 minutes
> 
> It's INSANE 🤯😳🫣 https://t.co/tIIfH076EH

38-second vertical product film in 45 minutes, plus the reply offering it as a paid service. The "turn it into revenue" proof. Place directly under this paragraph.

---

# Repos to clone

- Music video: https://github.com/JohnHeibel/PDoomVideo

- Starter: https://github.com/JohnHeibel/ClaudeAnimationBase

- Node canvas: https://github.com/buildwithhanif/claude-animation-skill

- Framework (html): https://github.com/heygen-com/hyperframes

- Framework (react): https://www.remotion.dev/docs/ai/skills

- Long form: https://github.com/WinterArc21/Battle-of-Austerlitz-Film

- Prompt library: https://github.com/guanmo-ai/awesome-ai-motion

- Dataset: https://github.com/athemeroy/awesome-opus-5-5-videos

---

# Conclusion: 

The one-liner gets you a clip. The harness gets you a studio.

Install the stack, steal a reference, write the state list, own the seek(t) engine, and make Opus watch its own frames until every score is 8. 

Then package it as a skill and never write the long prompt again.

Follow my Substack to get the latest articles on AI, vibe-coding, and agentic systems.
