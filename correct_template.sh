SUFFIX=".tmpl"
# PATH=$(pwd)
# echo $PATH
for FILE in $(ls)
do
    foo=${FILE%"$SUFFIX"}
    mv $FILE $foo
done