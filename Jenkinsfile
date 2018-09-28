node {

  def folder = 'betterself_backend'
  def branches = [
    'master': [
      'host': 'betterself.today',
      'url': 'https://betterself.today/',
      'pem': '/var/lib/jenkins/betterself-dev.pem'
    ],
  ]

  def branchName = env.BRANCH_NAME
  def branch = branches[env.BRANCH_NAME]
  def host = branch['host']
  def url = branch['url']
  def pem = branch['pem']

  try {
    stage 'build'

    sh '''ssh -T -oStrictHostKeyChecking=no -i "''' + pem + '''" ubuntu@''' + host + ''' << EOF
      cd ''' + folder + '''
      git checkout ''' + branch + '''
      git reset --hard
      git pull

      sudo python3.6 -m pip install -r requirements.txt
      sudo python3.6 -m pip install --ignore-installed stripe
      sudo python3.6 manage.py migrate
      sudo python3.6 manage.py collectstatic --noinput

      sudo python3.6 deploy/update_config.py --conf celery
      sudo python3.6 deploy/update_config.py --conf nginx --host ''' + host + '''
      sudo cp deploy/confs/betterself_super.conf /etc/supervisor/conf.d/

      sudo service supervisor restart
      sudo service nginx restart
    '''

    stage "slack"
    slackSend color: 'bad', message: "Backend deploy " + url + " is success!", channel: "#betterself_jenkins"

  } catch (err) {
    stage "slack"
    slackSend color: 'good', message: "Backend deploy " + url + " is FAILED!!! See console log in " + env.BUILD_URL + "console", channel: "#betterself_jenkins"
  }
}
