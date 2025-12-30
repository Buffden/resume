# Resume Repo

This repo keeps multiple versions of my resume in one place, so every change is tracked and can be pulled back anytime. It also ensures a cloud-hosted resume is always available.

## Files
- `frontend-resume.tex`
- `full-stack-resume.tex`
- `*.pdf` (compiled outputs)

## Build
```bashµ
pdflatex frontend-resume.texµµ
pdflatex full-stack-resume.tex
```µ

## Cleanµ
```bash
rm -f *.aux *.log *.fdb_latexmk *.fls *.synctex.gz
```
