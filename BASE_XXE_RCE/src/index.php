<?php
libxml_use_internal_errors(true);
$xml_data = file_get_contents('php://input');
if(empty($xml_data)){
    echo "empty!";
    exit;
}
$doc = simplexml_load_string($xml_data, 'SimpleXMLElement', LIBXML_NOENT);
if ($doc === false){
    echo "error to parse";
    foreach(libxml_get_errors() as $error){
        echo "\t", $error->message;
    }
}   else{
    echo "update success!";
    echo "welcome, " . $doc->name . ".\n";
}
?>
