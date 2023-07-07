echo "Source to deploy venv."
echo " deploy: source deploy_venv.sh"
echo " use it: source venv/bin/activate"
echo " exit it: deactivate"

# Path: source\venv\Scripts\activate
python3.11 -m venv imw_venv
source imw_venv/bin/activate
pip3.11 install -r requirements_imw_venv.txt -v

echo "Virtual environment is ready to use."