function install() {
   clear
   echo -e "\033[32m[~] Updating packets..."
   sudo apt update -y && sudo apt upgrade -y
  

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] python3 is installed"
   else
   echo -e "\033[31m\n[!] python3 isn't installed"
   sleep 2
   echo -e "\033[32m\n[~] Installing python3..."
   sudo apt install python3 -y
   fi
   
   sleep 3
   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] pip3 is installed"
   else
   echo -e "\033[31m\n[!] pip3 isn't installed"
   sleep 2
   echo -e "\033[32m\n[~] Installing pip3..."
   sudo apt install python3-pip -y
   fi
   
   echo -e "\033[32m\n[~] Installing requirements..."
   pip3 install -r requirements.txt
}

install
