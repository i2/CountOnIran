cat << EOF | sudo tee /etc/cron.d/iran
* * * * * echo $(date), $(python3 $HOME/countONiran/count.py) >> $HOME/iran.txt
EOF

#sudo rm /etc/cron.d/iran

