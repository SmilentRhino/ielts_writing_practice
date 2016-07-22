var markdownpdf = require("markdown-pdf")
  , fs = require("fs")
 
fs.createReadStream("/Users/mzzhang/ielts_writing_practice/ielts-mentor.com/ielts-mentor-cue-card-samples")
  .pipe(markdownpdf())
  .pipe(fs.createWriteStream("/Users/mzzhang/ielts_writing_practice/ielts-mentor.com/ielts-mentor-cue-card-samples.pdf"))
 
 
