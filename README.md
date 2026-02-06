# Resume Repo

This repo keeps multiple versions of my resume in one place, so every change is tracked and can be pulled back anytime. It also ensures a cloud-hosted resume is always available.

## VS Code Extension (Recommended)

I recommend using the **LaTeX Workshop** extension for VS Code. It provides an excellent LaTeX editing experience with build tasks, integrated PDF preview, and many productivity features.

**Install from the Marketplace:**
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

### Key Features

#### Build LaTeX to PDF automatically on save

![Build process](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/build.gif)

#### View PDF on-the-fly

![Preview feature](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/preview.gif)

#### Direct and reverse SyncTeX - Click to jump between source and PDF

![SyncTeX](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/synctex.gif)

#### Intellisense for citations and references

![Intellisense](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/ref.gif)

#### LaTeX log parser with automatic error reporting

![Error reporting](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/errors.png)

#### Linting support

![Chktex linting](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/chktex.gif)

#### Snippets and shortcuts

![Subparagraph snippet](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/subparagraph.gif)

#### Wrap text with LaTeX commands

![Wrap command](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/wrap.gif)

#### Greek letters and mathematical helpers

![Greek letters](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/greek%20letter.gif)

![Frac shortcut](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/frac.gif)

![Int shortcut](https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/int.gif)

## Files

- `frontend-resume.tex`
- `Harshwardhan-Patil-Resume.tex`
- `*.pdf` (compiled outputs)

## Build

From a terminal in this folder you can compile the TeX files to PDF:
```bash
pdflatex frontend-resume.tex
pdflatex Harshwardhan-Patil-Resume.tex
```

After running `pdflatex` you may need to run it a second time for references to settle.

## View PDF on macOS

- **Using Preview:** open the generated PDF (e.g. `open frontend-resume.pdf`) to view in macOS Preview.
- **Using VS Code:** the popular extension `LaTeX Workshop` provides build commands and an integrated PDF viewer. If you use VS Code on macOS, install `James-Yu.latex-workshop` and use the sidebar or the `LaTeX Workshop: Build LaTeX project` command to compile and preview.

If you use a different LaTeX extension on macOS, tell me its name and I'll update this README to mention it specifically.

## Clean

```bash
rm -f *.aux *.log *.fdb_latexmk *.fls *.synctex.gz
```

## Embedding GIFs in this README

You can embed animated GIFs in `README.md` either by linking to an externally hosted image or by adding the GIF file to this repo and referencing it locally. Examples:

- External link (hotlinking):

```markdown
![Resume preview GIF](https://example.com/path/to/animation.gif)
```

- Local file (recommended):

1. Create an `images/` folder in the repo, add the GIF (for example `images/resume-preview.gif`).
2. Reference it in the README:

```markdown
[![Resume preview](images/resume-preview.gif)](images/resume-preview.gif)
```

Notes:
- Hotlinking to images on other sites works if the image is publicly hosted, but availability and longevity depend on the remote host.
- Some sites disallow hotlinking or have licensing restrictions; prefer adding the GIF to your repo (or a reliable CDN) if you control the content.
- If the GIF is large, consider resizing/compressing it so GitHub renders quickly; for very large binary assets consider Git LFS.

If you want, I can add the screenshot/gif you uploaded into `images/resume-preview.png` or `images/resume-preview.gif` and update the README to show it.
