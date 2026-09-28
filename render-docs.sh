#!/bin/sh
# Double-clickable renderer: rebuilds the documentation HTML pages and
# pops up a summary window. Right-click in Files and choose
# "Run as a Program" (or run ./render-docs.sh in a terminal).
cd "$(dirname "$0")"
if out=$(python3 docs/render.py 2>&1); then
  zenity --info --title "Render docs" --text "Done.\n\n$out" --width=420 2>/dev/null
else
  zenity --error --title "Render docs" --text "Failed:\n\n$out" --width=420 2>/dev/null
fi
