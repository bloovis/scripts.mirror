#!/usr/bin/perl

# This is CGI script that allows you to post URLs for naughty web sites on Reddit
# or Twitter, bypassing those sites' censor-bots.

# Top level URL for your web site.
my $site = 'https://www.example.com';

use CGI qw(:standard);

local ($value);

# Replace special characters with http escape sequences.
sub escape {
  my $value = shift;
  $value =~ s/:/%3A/g;
  $value =~ s/\//%2F/g;
  $value =~ s/#/%23/g;
  return($value);
}

# Replace http escape sequences with their ASCII equivalents.
sub unescape {
  my $value = shift;
  $value =~ s/%3A/:/g;
  $value =~ s/%2F/\//g;
  $value =~ s/%23/#/g;
  return($value);
}

# Replace a "naughty" URL with a censorship-avoiding one.
sub fixurl {
  my $url = shift;
  my $base = "$site/redirect.cgi?";

  if ($url =~ /^https:\/\/www.bitchute.com\/video\/([^\/]+)/) {
    return ($base . "b=" . $1);
  } elsif ($url =~ /^https:\/\/rumble.com\/(.*)/) {
    return ($base . "r=" . $1);
  } elsif ($url =~ /^https:\/\/brandnewtube.com\/(.*)/) {
    return ($base . "bnt=" . $1);
  } elsif ($url =~ /^https:\/\/rt.com\/(.*)/) {
    return ($base . "rt=" . $1);
  } elsif ($url =~ /^https:\/\/www.zerohedge.com\/(.*)/) {
    return ($base . "z=" . $1);
  } elsif ($url =~ /^https:\/\/www.thegatewaypundit.com\/(.*)/) {
    return ($base . "g=" . $1);
  } elsif ($url =~ /^https:\/\/1drv.ms\/(.*)/) {
    return ($base. "od=" . $1);
  } elsif ($url =~ /^(.*)substack.com\/(.*)/) {
    return ($base . "s=" . escape($1 . '#' . $2));
  } else {
    return ($url);
  }
}

sub redir {
  my ($url, $query) = @_;
  print "Content-type: text/html\n\n";
  print qq[
<!DOCTYPE html>
<html>
  <head>
];
  if ($url) {
    print qq[
<meta http-equiv="refresh" content="1; url='$url'" />
];
  }
  print qq[
  </head>
  <body>
<h1>Anti-censorship URL redirector</h1>
];
  if ($query) {
    my $fixedurl = fixurl($query);
    print qq[
<p>You entered $query .</p>
<p>The fixed URL is <a href="$fixedurl">$fixedurl</a> .</p>
];
  }
  print qq[
<h2>Form</h2>

<p>Enter a URL to get a Reddit-safe URL</p>

<form action="/redirect.cgi">
  <input type="text" id="q" name="q" size="50"><br/>
  <input type="submit" value="Submit">
</form>

<h2>Usage</h2>

<h3>BitChute</h3>
<p>Put the BitChute video id in this page's <code>b</code> parameter.</p>

<p>To link to:</p>
<ul>
<li>https://www.bitchute.com/video/<b>36rBJ1ve8BFQ</b>/
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?b=36rBJ1ve8BFQ">$site/redirect.cgi?b=<b>36rBJ1ve8BFQ</b></a>
</ul>

<h3>Rumble</h3>
<p>Put everything after the https://rumble.com/ in this page's <code>r</code> parameter.</p>

<p>To link to:</p>
<ul>
<li>https://rumble.com/<b>viwogh-breaking-now-canada-completely-bans-free-speech-overnight-passes-bill-at-13.html</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?r=viwogh-breaking-now-canada-completely-bans-free-speech-overnight-passes-bill-at-13.html">$site/redirect.cgi?r=<b>viwogh-breaking-now-canada-completely-bans-free-speech-overnight-passes-bill-at-13.html</b></a>
</ul>

<h3>BrandNewTube</h3>
<p>Put everything after the https://brandnewtube.com/ in this page's <code>bnt</code> parameter.</p>

<p>To link to:</p>
<ul>
<li>https://brandnewtube.com/<b>watch/whatsherface-digital-currency_eoIzW2cHS9HzgQ7.html</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?bnt=watch/whatsherface-digital-currency_eoIzW2cHS9HzgQ7.html">
$site/redirect.cgi?bnt=<b>watch/whatsherface-digital-currency_eoIzW2cHS9HzgQ7.html</b></a>
</ul>

<h3>RT</h3>
<p>Put the article path in this page's <code>rt</code> parameter.</p>
<p>To link to:</p>
<ul>
<li>https://rt.com/<b>business/551241-gas-price-record-europe/</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?rt=business/551241-gas-price-record-europe/"
  >$site/redirect.cgi?rt=<b>business/551241-gas-price-record-europe/</b></a>
</ul>

<h3>Zero Hedge</h3>
<p>Put the article path in this page's <code>z</code> parameter.</p>
<p>To link to:</p>
<ul>
<li>https://www.zerohedge.com/<b>covid-19/dr-fauci-cant-explain-why-texas-covid-cases-keep-dropping-despite-reopening</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?z=covid-19/dr-fauci-cant-explain-why-texas-covid-cases-keep-dropping-despite-reopening"
  >$site/redirect.cgi?z=<b>covid-19/dr-fauci-cant-explain-why-texas-covid-cases-keep-dropping-despite-reopening</b></a>
</ul>

<h3>Gateway Pundit</h3>
<p>Put the article path in this page's <code>g</code> parameter.</p>
<p>To link to:</p>
<ul>
<li>https://www.thegatewaypundit.com/<b>2021/11/robert-f-kennedy-jr-building-totalitarian-state-armageddon-final-battle-need-win-one-video/</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?g=2021/11/robert-f-kennedy-jr-building-totalitarian-state-armageddon-final-battle-need-win-one-video/"
  >$site/redirect.cgi?g=<b>2021/11/robert-f-kennedy-jr-building-totalitarian-state-armageddon-final-battle-need-win-one-video/</b></a>
</ul>

<h3>OneDrive</h3>
<p>Put everything after the https://1drv.ms/ in this page's <code>od</code> parameter.</p>

<p>To link to:</p>
<ul>
<li>https://1drv.ms/<b>b/s!Au6KGoaF2jo-8ljmk2KNQSFKGBIE</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?od=b/s!Au6KGoaF2jo-8ljmk2KNQSFKGBIE"
  >$site/redirect.cgi?od=<b>b/s!Au6KGoaF2jo-8ljmk2KNQSFKGBIE</b></a>
</ul>

<h3>Substack</h3>
<p>Replace substack.com/ with #.  Then replace all / characters with %2F,
and replace all : characters with %3A.  Put the result in this page's
<code>s</code> parameter.</p>

<p>To link to:</p>
<ul>
<li>https://boriquagato.substack.com/p/bluebird-bans-are-back</b>
</ul>
<p>Use:</p>
<ul>
<li><a href="$site/redirect.cgi?s=https%3A%2F%2Fboriquagato.%23p%2Fbluebird-bans-are-back"
  >$site/redirect.cgi?s=https%3A%2F%2Fboriquagato.%23p%2Fbluebird-bans-are-back</b></a>
</ul>
</body>
</html>
];
}

if ($value = param('b')) {
  redir('https://www.bitchute.com/video/' . $value);
} elsif ($value = param('r')) {
  redir('https://rumble.com/' . $value);
} elsif ($value = param('z')) {
  redir('https://www.zerohedge.com/' . $value);
} elsif ($value = param('bnt')) {
  redir('https://brandnewtube.com/' . $value);
} elsif ($value = param('rt')) {
  redir('https://rt.com/' . $value);
} elsif ($value = param('g')) {
  redir('https://www.thegatewaypundit.com/' . $value);
} elsif ($value = param('od')) {
  redir('https://1drv.ms/' . $value);
} elsif ($value = param('s')) {
  $value = unescape($value);
  if ($value =~ /(.*)#(.*)/) {
    redir($1 . 'substack.com/' . $2);
  } else {
    redir(undef, 'Bad substack URL: ' . $value);
  }
} elsif ($value = param('q')) {
  redir(undef, $value);
} else {
  redir(undef);
}
1;
