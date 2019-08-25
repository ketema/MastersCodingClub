#!/opt/local/bin/php

<?php
    function readListOfGrades( $file ){
        $gradeList = fopen($file, "r");
        $numGrades = fgets($gradeList);

        while(!feof($gradeList)) {
            $grade = fgets($gradeList);
            determinePassFail($grade);
        }
        
        fclose($gradeList);
    }

    function determinePassFail( $grade ){
        if ( $grade >= 70 ){
            echo( "PASS\n");
        }
        else{
            echo("FAIL\n");
        }
    }

    readListOfGrades("../Prob01.in.txt");
?>