module.exports = function (grunt) {
  grunt
    .initConfig({
      "couch-compile": {
        dbs: {
          files: {
            "/tmp/covid_twitter.json":"covid_twitter",
            "/tmp/beer_twitter.json":"beer_twitter",
            "/tmp/income_twitter.json":"income_twitter",
            "/tmp/all_twitter.json":"all_twitter"
          }
        }
      },
      "couch-push": {
        options: {
          user: "admin",
          pass: "admin"
        }
      }
    });
  grunt.config.set(`couch-push.covid_twitter.files.http://172\\.26\\.128\\.223:5984/covid_twitter`, "/tmp/covid_twitter.json");
  grunt.config.set(`couch-push.beer_twitter.files.http://172\\.26\\.128\\.223:5984/beer_twitter`, "/tmp/beer_twitter.json");
  grunt.config.set(`couch-push.income_twitter.files.http://172\\.26\\.128\\.223:5984/income_twitter`, "/tmp/income_twitter.json");
  grunt.config.set(`couch-push.all_twitter.files.http://172\\.26\\.128\\.223:5984/all_twitter`, "/tmp/all_twitter.json");

console.log(JSON.stringify(grunt.config.get()));
  grunt.loadNpmTasks("grunt-couch");
};
