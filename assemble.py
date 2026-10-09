from pathlib import Path
import json
scripts=['vendor/docx.js','word-export.js','sections.js','engine.js','app.js','enhancements-existing.js','regulatory.js']
s=Path('shell.html').read_text()
code='\n'.join('<script>\n'+Path(f).read_text()+'\n</script>' for f in scripts)
code+='<script>const PARAMETER_HELP='+Path('parameter-help.json').read_text()+';</script>'
code+='<script>'+Path('upgrade.js').read_text()+'</script>'
if Path('tutorial-player.js').exists():code+='<script>'+Path('tutorial-player.js').read_text()+'</script>'
Path('index.html').write_text(s.replace('__SCRIPTS__',code))
