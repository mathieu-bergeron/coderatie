for i in *.tex; 
do 
    pdflatex $i;
done


for i in *.pdf; 
do 
    convert -density 300 $i -quality 100 -antialias $(echo $i | sed "s/pdf/png/"); 
done
