#ifndef CONTA_POUPANCA_H
#define CONTA_POUPANCA_H

#include "Conta.h"

#include <iostream>
using std::cout;
using std::endl;

class ContaPoupanca : public Conta
{
public:
  ContaPoupanca(int conta, string nome, string aniversario, double saldo = 0.0) : Conta(conta, nome, saldo),aniversario(aniversario) {}
  
  virtual ~ContaPoupanca(){}


  virtual void extrato()
  {
    cout << "CONTA: " << conta << endl;
    cout << "CLIENTE: " << nome << endl;
    cout << "ANIVERSARIO: " << aniversario << endl;
    cout << "Transações: " << endl;
    for (int i = 0 ; i < tTransacoes ; i++)
      cout << op[i].data << " " << op[i].valor << " " << op[i].descricao << endl;
    cout << "------------------------------" << endl;
    cout << "Saldo: R$ " << saldo << endl;
  }

private:
  string aniversario;
};

#endif