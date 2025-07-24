# LaTeX Resume Project

A LaTeX-based resume project with multiple resume templates and PDF generation capabilities.

## Overview

This project contains LaTeX resume templates that can be compiled to PDF using MacTeX (macOS LaTeX distribution).

## Files

### Resume Templates
- `full-stack-resume.tex` - Full-stack developer resume template
- `frontend-resume.tex` - Frontend developer resume template

### Generated PDFs
- `full-stack-resume.pdf` - Compiled full-stack resume
- `frontend-resume.pdf` - Compiled frontend resume



## Setup

### Prerequisites
- **MacTeX** - LaTeX distribution for macOS
  - Download from: https://www.tug.org/mactex/
  - Or install via Homebrew: `brew install --cask mactex`

### Installation
1. Install MacTeX following the official instructions
2. Verify installation: `pdflatex --version`

## Usage

### Compile PDFs
```bash
# Compile full-stack resume
pdflatex full-stack-resume.tex

# Compile frontend resume  
pdflatex frontend-resume.tex
```

### View PDFs
- Open the generated `.pdf` files in any PDF viewer
- Use Preview.app (default on macOS)
- Or use VS Code with PDF viewer extension

### Clean Up
Remove LaTeX compilation artifacts:
```bash
rm -f *.aux *.log *.fdb_latexmk *.fls *.synctex.gz
```

## Project Structure

```
resume/
├── full-stack-resume.tex    # Full-stack developer resume
├── frontend-resume.tex      # Frontend developer resume
├── *.pdf                   # Generated PDF files
└── README.md              # This file
```

## Features

- **Multiple Templates**: Different resume styles for different roles
- **Professional Formatting**: Clean, modern LaTeX styling
- **PDF Output**: High-quality PDF generation
- **Cross-platform**: Works on macOS, Linux, and Windows
- **Future Integration**: Planning to integrate n8n for workflow automation and infinite possibilities

## LaTeX Packages Used

- `geometry` - Page layout and margins
- `titlesec` - Section title formatting
- `tabularx` - Advanced table formatting
- `xcolor` - Color support
- `fontawesome5` - Icons
- `hyperref` - Hyperlinks and PDF metadata
- `paracol` - Multi-column layout
- `charter` - Professional font

## Future Plans

### n8n Integration
This project is planned to integrate with **n8n** (workflow automation platform) to enable:
- **Automated PDF generation** and distribution
- **Dynamic content updates** based on external data sources
- **Multi-format export** (PDF, HTML, DOCX)
- **Version control integration** with automated deployments
- **Custom workflows** for resume management and distribution

The integration will open up infinite possibilities for resume automation and management workflows.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test compilation
5. Submit a pull request

## License

This project is open source and available under the MIT License.