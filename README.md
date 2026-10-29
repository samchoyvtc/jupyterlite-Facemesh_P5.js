# p5.js FaceMesh — 45-minute class

A JupyterLite site for one 45-minute class. Students open a working p5.js sketch, allow the camera, and edit a few lines so ml5 FaceMesh draws points on their face.

Live site (after a push to `main`):

**https://samchoyvtc.github.io/jupyterlite-Facemesh_P5.js/**

## Class shape

| Time | What students do |
| --- | --- |
| 0–8 min | Open `facemesh.ipynb`, run every code cell, allow the camera |
| 8–18 min | Follow four ideas: `setup`, `draw`, `ml5.faceMesh`, and the keypoint loop |
| 18–30 min | Change point size and color, then run that cell again |
| 30–42 min | Turn on the nose and eye marks |
| 42–45 min | Show the sketch to a neighbor |

The camera stream and the face model stay in the browser.

## What is in the site

- [content/README.md](content/README.md) — the three steps students see in the file browser
- [content/facemesh.ipynb](content/facemesh.ipynb) — the only lesson
- [content/reference/landmarks.md](content/reference/landmarks.md) — nose and eye point numbers

Lesson code avoids backticks. The p5 kernel replays cells inside a template string, so a backtick in a cell breaks the sketch.

## Deploy

GitHub Actions builds this folder with JupyterLite and publishes `dist/` to GitHub Pages on every push to `main`. Pages must use **GitHub Actions** as the source.

```bash
python -m pip install -r requirements.txt
jupyter lite build --contents content --output-dir dist
```
