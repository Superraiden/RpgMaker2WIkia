@echo off 
mogrify -path . -trim *
FORFILES /M *.png /c "cmd /c convert @FILE -virtual-pixel background -background none -set option:distort:viewport "%[fx:max(w,h)]x%[fx:max(w,h)]-%[fx:max((h-w)/2,0)]-%[fx:max((w-h)/2,0)]" -filter point -distort SRT 0 +repage @FILE"