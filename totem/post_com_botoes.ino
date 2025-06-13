/*
 * Método POST no ESP-32 rodando com API Flask (Python).
 * 03 botões na protoboard para receber os inputs. 
 * LCD para mostrar mensagem amigável ao usuário.
 * Necessário importar o config.h com os dados da rede.
 */

// INCLUSÃO DE BIBLIOTECAS
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "config.h"

// DISPLAY LCD
#define endereco  0x27 // Endereços comuns: 0x27, 0x3F
#define colunas   16
#define linhas    2

// BOTOES 
#define btn_01 15
#define btn_02 2
#define btn_03 4

const char* ssid = WIFI_SSID;
const char* pass = WIFI_PASSWORD;

// INSTANCIANDO OBJETOS
LiquidCrystal_I2C lcd(endereco, colunas, linhas);

void setup() {

  // set LCD
  lcd.init(); // INICIA A COMUNICAÇÃO COM O DISPLAY
  lcd.setBacklight(HIGH); // LIGA A ILUMINAÇÃO DO DISPLAY
  lcd.setCursor(0, 0);
  lcd.print("Inicializando...");
  delay(1000);

  // Set pin mode
  pinMode(btn_01, INPUT_PULLUP);
  pinMode(btn_02, INPUT_PULLUP);
  pinMode(btn_03, INPUT_PULLUP);

  // Start Serial conn
  Serial.begin(921600);

  // Conexao com WiFi
  WiFi.begin(ssid, pass);
  Serial.print("Conectando ao WiFi...");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("\nWiFi Conectado!");
  Serial.print("IP Local: ");
  Serial.println(WiFi.localIP());

  // limpar LCD:
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("De seu feedback");
}

void mostrarMensagem() {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Agradecemos o ");
    lcd.setCursor(0, 1);
    lcd.print("Feedback! ");
    delay(5000);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("De seu feedback");
}

void httpPOST(char feedback) {
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(ENDPOINT);
      http.addHeader("Content-Type", "application/json");

      Serial.println("Enviando requisição...");

      String pos = "{\"status\":\"positivo\"}";
      String neu = "{\"status\":\"neutro\"}";
      String neg = "{\"status\":\"negativo\"}";

      int httpResponseCode;

      if (feedback == 'p') {
        httpResponseCode = http.POST(pos);
      } else if (feedback == 'm') {
        httpResponseCode = http.POST(neu);
      } else if (feedback == 'n') {
        httpResponseCode = http.POST(neg);
      } else {
        httpResponseCode = 500;
      }

      if (httpResponseCode > 0) {
        Serial.print("Código de resposta: ");
        Serial.println(httpResponseCode);
        String response = http.getString();
        Serial.println("Resposta do servidor: " + response);
      } else {
        Serial.print("Erro na requisição: ");
        Serial.println(httpResponseCode);
      }

      http.end();
    } else {
      Serial.println("Erro: WiFi desconectado!");
    }
}

void loop() {
  bool positivo = digitalRead(btn_01);       
  bool neutro = digitalRead(btn_02);       
  bool negativo = digitalRead(btn_03);       

  if (positivo == true) {                    
    Serial.println("positivo clicado");
    httpPOST('p');
    mostrarMensagem();                           
  }
  if (neutro == true) {                    
    Serial.println("neutro clicado");
    httpPOST('m');  
    mostrarMensagem();                           
  }
  if (negativo == true) {                    
    Serial.println("negativo clicado"); 
    httpPOST('n');
    mostrarMensagem();                          
  }
}