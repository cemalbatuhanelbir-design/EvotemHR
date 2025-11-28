#!/bin/bash
# Rebranding script: Horilla -> EVOTEM HR

echo "Starting rebranding process..."
echo "This will replace all instances of Horilla with EVOTEM HR in files"
echo ""

# Counter for modified files
count=0

# Find all relevant files (excluding venv, .git, node_modules, media)
find . -type f \( \
    -name "*.py" -o \
    -name "*.html" -o \
    -name "*.js" -o \
    -name "*.css" -o \
    -name "*.md" -o \
    -name "*.txt" -o \
    -name "*.json" -o \
    -name "*.yml" -o \
    -name "*.yaml" \
\) \
    ! -path "./venv/*" \
    ! -path "./.git/*" \
    ! -path "./node_modules/*" \
    ! -path "./media/*" \
    ! -path "./static/build/*" \
    -print0 | while IFS= read -r -d '' file; do
    
    # Check if file contains any variant of "horilla"
    if grep -qi "horilla" "$file" 2>/dev/null; then
        
        # Perform replacements
        # HORILLA -> EVOTEM_HR (for constants, env vars)
        # Horilla -> EVOTEM HR (for display names, titles)
        # horilla -> evotem_hr (for module names, identifiers)
        
        sed -i \
            -e 's/HORILLA/EVOTEM_HR/g' \
            -e 's/Horilla/EVOTEM HR/g' \
            -e 's/horilla/evotem_hr/g' \
            "$file"
        
        count=$((count + 1))
        echo "Modified: $file"
    fi
done

echo ""
echo "Rebranding complete!"
echo "Total files modified: $count"
