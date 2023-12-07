/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;

#include <iomanip>
using namespace std;

#include <fstream>
using namespace std;

#include <string>
using namespace std;

#include <stdexcept>
using namespace std;

#include "Pessoa.h"
#include "PessoaFisica.h"
#include "PessoaJuridica.h"
#include "Conta.h"
#include "ContaCorrente.h"
#include "ContaPoupanca.h"
#include "ContaLimite.h"
#include "Excecao.h"
#include "Banco.h"

int main()
{
  fstream fileIO ("DadosBanco.dat", ios::out | ios::in);

  //if (!fileIO)
  //  fileIO.open("DadosBanco.dat", ios::out);

  if (!fileIO)
    return 1;
    
//Ajustar visao do gerente e visao do cliente, e ajustar salvamento/exclusao de dados no arquivo DadosBanco para cada caso
//Ajustar a logica faltante das etapas em ambas as visoes

  int posicao;
  Banco banco ("Bradesco", lista1, lista2);
  cout << "Aponte sua posicao: 1- Gerente do banco  2- Cliente do banco" << endl;
  cin >> posicao;
  
  if(posicao == 1){
      
   while(1){
    cout << "----------visão gerente----------" << endl;
      cout << "Banco " << banco.nomeBanco << endl;
      cout << "Opcoes:" << endl;
      cout << "1 - Abrir conta" << endl;
      cout << "2 - Atualizar conta" << endl;
      cout << "3 - Consultar conta" << endl;
      cout << "4 - Fechar conta" << endl;
      cout << endl << "-1 - Sair" << endl;
      cout << "Op: ";  
      int op;
      cin >> op;
      
      switch (op)
	{
	case 1:
	  {
	    int aux;
	    cout << "Tipo de conta: 1- Conta Corrente  2- Conta Limite  3- Conta Poupanca" << endl;
	    cin >> aux;

	    if (aux == 1){
	      ////ContaCorrente x;
	    }
	    if (aux == 2){
	      //ContaLimite x;
	    }
	    if (aux == 3){
          //ContaPoupanca x;
	    }
	    break;
	  }
	case 2:
	  {
	    int aux;
	    int numconta;
	    cout << "Tipo de conta: 1- Conta Corrente  2- Conta Limite  3- Conta Poupanca" << endl;
	    cin >> aux;

	    if (aux == 1){
	      cout << "Informe o numero da conta: " << endl;
	      cin >> numconta;
	      //atualizar
	    }

	    if (aux == 2){
	      cout << "Informe o numero da conta: " << endl;
	      cin >> numconta;
	      //atualizar
	    }

	    if (aux == 3){
	      cout << "Informe o numero da conta: " << endl;
	      cin >> numconta; 
	      //atualizar
	    }
	    break;
	  }
	case 3:
	  {
	    int aux;
	    cout << "Informe o numero da conta: " << endl;
	    cin >> aux;
	    //ContaEmQuestao.exibirdados()
	    //atualizar
	    
	  }
		break;
	case 4:
	{
	    int aux;
	    cout << "Informe o numero da conta: " << endl;
	    cin >> aux;
	    //ContaEmQuestao Invoca destrutor
	    //atualizar
		break;
	      }
	case -1:
	      fileIO.close ();
	      exit (0);
	      break;

	default:
	      //
	      break;
	    }
  }
}
	    
if(posicao == 2){
    int numconta;
    cout << "Informe o numero da sua conta: " << endl;
    cin >> numconta;
    //acrescentar excecao para caso de contanaoencontrada
    
  while (1)
    {
      cout << "----------visão cliente----------" << endl;
      cout << "Banco " << banco.nomeBanco << endl;
      cout << "Opcoes:" << endl;
      cout << "1 - Saque" << endl;
      cout << "2 - Deposito" << endl;
      cout << "3 - Transferencia entre contas" << endl;
      cout << "4 - Exibir o extrato" << endl;
      cout << "5 - Exibir Saldo" << endl;
      cout << endl << "-1 - Sair" << endl;
      cout << "Op: ";
      int op;
      cin >> op;


      switch (op)
	{
	case 1:
	  {
	    int aux;
	    double valor;
	    cout << "Se sua conta for Conta Corrente, digite 1" << endl << "Se sua conta for Conta com Limite, digite 2" << endl << "Se sua conta for Conta PoupanC'a, digite 3" << endl;
	    cin >> aux;

	    if (aux == 1){
	      cout << "Informe o valor para saque:" << endl;
	    cin >> valor;
	    try{
	    ContaCorrente x >> valor;
	    }
	    catch (SaldoInsuficiente & e)
	    {
	      cerr << e.what () << endl;
	    }
	    catch (ExcedeLimite & e)
	      {
	          cerr << e.what() << endl;
	      }}
	    

	    if (aux == 2){
	      cout << "Informe o valor para saque:" << endl;
	    cin >> valor;
	    try{
	    ContaLimite x >> valor;
	    }
	    catch (SaldoInsuficiente & e)
	    {
	      cerr << e.what () << endl;
	    }}

	    if (aux == 3){
	      cout << "Informe o valor para saque:" << endl;
	    cin >> valor;
	    try{
	    ContaPoupanca x >> valor;
	    }
	    catch (SaldoInsuficiente & e)
	    {
	      cerr << e.what () << endl;
	    }}

	    break;
	  }
	case 2:
	  {
	    int aux;
	    double valor;
	    cout << "Se sua conta for Conta Corrente, digite 1" << endl << "Se sua conta for Conta com Limite, digite 2" << endl << "Se sua conta for Conta PoupanC'a, digite 3" << endl;
	    cin >> aux;

	    if (aux == 1){
	      cout << "Informe o valor sendo depositado: " << endl;
	    cin >> valor;
	    ContaCorrente x << valor;}

	    if (aux == 2){
	      cout << "Informe o valor sendo depositado: " << endl;
	    cin >> valor;
	    ContaLimite x << valor;}

	    if (aux == 3){
	      cout << "Informe o valor sendo depositado: " << endl;
	    cin >> valor;
	    ContaPoupanca x << valor;}
	    break;
	  }
	case 3:
	  {
	    int aux;
	    int aux2;
	    double valor;
	    cout << "Se sua conta for Conta Corrente, digite 1" << endl << "Se sua conta for Conta com Limite, digite 2" << endl << "Se sua conta for Conta PoupanC'a, digite 3" << endl;
	    cin >> aux;

	    if (aux == 1){
	    cout <<"Informe o tipo de conta que recebera a transferencia: 1- ContaCorrente  2- Conta c/ Limite  3- Conta Poupanca" << endl;
	    cin >> aux2;
	    cout << "Informe o valor sendo transferido:" << endl;
	    cin >> valor;
	    try
	    {
	      ContaCorrente x >> valor;
	    }
	    catch (SaldoInsuficiente & e)
	    {
	      cerr << e.what () << endl;
	    }
	    if(aux2 == 1)
          ContaCorrente x << valor;
        if(aux2 == 2)
          ContaLimite y << valor;
        if(aux2 == 3)
          ContaPoupanca z << valor;
	    }
	    
	    
	      if (aux == 2){
		cout << "Informe o tipo de conta que recebera a transferencia: 1- ContaCorrente  2- Conta c/ Limite  3- Conta Poupanca" << endl;
	      cin >> aux2;
	      cout << "Informe o valor sendo transferido:" << endl;
	      cin >> valor;
	      try
	      {
		ContaLimite y >> valor;
	      }
	      catch (SaldoInsuficiente & e)
	      {
		cerr << e.what() << endl;
	      }
	      catch (ExcedeLimite & e)
	      {
	          cerr << e.what() << endl;
	      }
	    if(aux2 == 1)
          ContaCorrente x << valor;
        if(aux2 == 2)
          ContaLimite y << valor;
        if(aux2 == 3)
          ContaPoupanca z << valor;
	    }

		if (aux == 3){
		  cout << "Informe o tipo de conta que recebera a transferencia: 1- ContaCorrente  2- Conta c/ Limite  3- Conta Poupanca" << endl;
		cin >> aux2;
		cout << "Informe o valor sendo transferido:" << endl;
		cin >> valor;
		try
		{
		  ContaPoupanca z >> valor;
		}
		catch (SaldoInsuficiente &e)
        {
          cerr << e.what() << endl;
        }
        if(aux2 == 1)
          ContaCorrente x << valor;
        if(aux2 == 2)
          ContaLimite y << valor;
        if(aux2 == 3)
          ContaPoupanca z << valor;
		}

		break;
	      }
	case 4:
	{
	       //contaemquestao.extrato();
		break;
	      }
	case 5:
	{
	      //cout << "Saldo da conta: " << contaemquestao.saldo << endl;
		break;
	      }
	case -1:
	      fileIO.close ();
	      exit (0);
	      break;

	default:
	      //
	      break;
	    }
	  }
        }
	  return 0;
	}