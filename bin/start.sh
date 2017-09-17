source activate 3.6
./bin/runDockerSentiment.sh
./bin/runDockerLinear.sh
python manage.py runserver 0.0.0.0:8000
