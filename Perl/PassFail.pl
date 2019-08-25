#!/opt/local/bin/perl

open(my $gradeList, '<:encoding(UTF-8)', "../Prob01.in.txt")
    or die "Could Not Open File";

my $numGrades = <$gradeList>;

while (my $grade = <$gradeList>){
    if ( $grade >= 70 ){
        print "PASS\n";
    }
    else{
        print "FAIL\n";
    }
}