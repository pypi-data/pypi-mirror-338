#python3 -c "import pkg_resources;\
#from pkg_resources import DistributionNotFound, VersionConflict;\
#dependencies = [\
#  'Werkzeug>=0.6.1',\
#  'Flask>=0.9',\
#];\
#print('test');\
#print(pkg_resources.require(dependencies));\
#"
##python3 -c "print('test')"
python3 -m pip check ../requirements.txt
echo $#
