function (doc) {
    doc.text.toLowerCase().split(/\W+/).forEach(function (word){
        if(word.length > 1){
            emit([word, doc.lang],1);
        }
    });
}