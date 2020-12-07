./creer_graphes.py
for i in *.pdf; 
do 
    convert  $i $(echo $i | sed "s/pdf/png/"); 
done
