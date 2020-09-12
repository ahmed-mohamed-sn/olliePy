#sphinx-build -b html ./sphinxSource/source ./docs
cd sphinxSource && make clean && make html && touch ../docs/.nojekyll
