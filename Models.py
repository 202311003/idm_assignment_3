from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Winner(BaseModel):
    Team_1_Encoded: str 
    Team_2_Encoded: str