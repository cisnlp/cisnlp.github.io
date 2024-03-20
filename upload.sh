#!/bin/bash

chmod a+r thesis_proposals/ -R
chmod a+r presentations/ -R

JEKYLL_ENV=production bundle exec jekyll build

cd _site/
rsync -avv ./ yihong@marmolata.cis.lmu.de:/srv/www/vhosts/schuetze/htdocs
cd ..
