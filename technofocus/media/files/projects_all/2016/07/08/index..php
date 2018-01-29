<?php

/* 
 * Redirect to a different page in the current directory that was requested 
 */
$host  = $_SERVER['HTTP_HOST'];
$uri  = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
$extra = 'page-scroll-effects/index2.html';  // change accordingly

header("Location: http://$host$uri/$extra");
exit;
/* Make sure that code below does not get executed when we redirect. */
exit;
?>