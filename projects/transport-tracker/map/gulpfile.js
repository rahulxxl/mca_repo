const gulp = require('gulp');
const less = require('gulp-less');
const serve = require('gulp-serve');
const path = require('path');

gulp.task('less-compile', () => {
  return gulp
    .src('./less/**/*.less')
    .pipe(
      less({
        paths: [path.join(__dirname, 'less', 'includes')]
      })
    )
    .pipe(gulp.dest('./css'));
});

gulp.task(
  'serve',
  ['less-compile'],
  serve({
    root: ['.'],
    port: 8080
  })
);
