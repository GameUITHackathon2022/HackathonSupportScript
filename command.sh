while read -r com; 
do 
    $com; 
    $echo $com
done < commands_archive.txt
cmd /k