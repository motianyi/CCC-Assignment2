module.exports = function (grunt) {
  grunt
    .initConfig({
      "couch-compile": {
        dbs: {
          files: {
            "/tmp/twitter.json": "couchdb"
          }
        }
      },
      "couch-push": {
        options: {
          user: "admin",
          pass: "admin"
        },
        twitter: {
        }
      }
    });
    
  grunt.config.set(`couch-push.twitter.files.http://172\\.26\\.128\\.223:5984/twitter`, "/tmp/twitter.json");
console.log(JSON.stringify(grunt.config.get()));
  grunt.loadNpmTasks("grunt-couch");
};
