$files = Get-ChildItem -Path . -Recurse -Filter *.html | Where-Object { $_.FullName -notmatch 'assets' -and $_.FullName -notmatch '.gemini' }

foreach ($f in $files) {
    if ($f.Name -ne 'ppe.html') {
        $content = Get-Content $f.FullName -Raw
        
        # Remove PPE link entirely
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)[ \t]*<li><a href="[^"]*ppe\.html">Учёт спецодежды</a></li>\s*', "`n")
        
        # Rename RFID link text
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '<li><a href="([^"]*rfid\.html)">RFID-решения</a></li>', '<li><a href="$1">RFID и спецодежда</a></li>')
        
        [System.IO.File]::WriteAllText($f.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($f.FullName)"
    }
}
Write-Host "Done"
