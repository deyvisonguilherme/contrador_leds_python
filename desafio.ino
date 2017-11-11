char dado;
byte pinos[] = {6, 7, 8, 9, 10, 11, 12, 13};

void setup() 
{
  Serial.begin(9600);
  
  for (int x=0; x<=7; x++)
  {
    pinMode(pinos[x], OUTPUT);
  }
}


void loop() 
{

  if (Serial.available() == 8) 
  {
    for(char i=0; i<=7; i++)
    {
      dado = Serial.read();
      
      switch(dado)
      {
        case '1':
          digitalWrite(pinos[i], HIGH);
        break;
        case '0':
          digitalWrite(pinos[i],LOW);
        break;
        case '2':
           apaga_tudo();
           first_sequencial();
        break;
        case '3':
          apaga_tudo();
          second_sequencial();
        break;
        case '4':
          apaga_tudo();
        break;
      }
    }
  }
}


void first_sequencial()
{
  for(int y=0; y<=7; y++)
   {
    digitalWrite(pinos[y], HIGH);
    delay(500);
    digitalWrite(pinos[y], LOW);
   }
}

void second_sequencial()
{
  for(int y=0; y<=7; y++)
  {
    digitalWrite(pinos[y], HIGH);
    delay(700);
  }
}

void apaga_tudo()
{
  for(int y=0; y<=7; y++)
  {
    digitalWrite(pinos[y], LOW);
  }
}

