#!/bin/bash
#    .---------- constant part!
#    vvvv vvvv-- the code from above
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Creating virtual environment...${NC}"
python3 -m venv env
source ./env/bin/activate
pip3 install gensim
pip3 install plotly
pip3 install scikit-learn
pip3 install numpy
pip3 install pandas
echo -e "${YELLOW}Virtual environment created${NC}"
echo -e "${YELLOW}Please run \"source env/bin/activate\" to activate it${NC}"