public class Veiculo {
    private String placa;
    private String tipo;
    private int numOcorrencias;
    private int anoFabricacao;

    public Veiculo(String placa, String tipo, int numOcorrencias, int anoFabricacao) {
        this.placa = placa;
        this.tipo = tipo;
        this.numOcorrencias = numOcorrencias;
        this.anoFabricacao = anoFabricacao;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getNumOcorrencias() {
        return numOcorrencias;
    }

    public void setNumOcorrencias(int numOcorrencias) {
        this.numOcorrencias = numOcorrencias;
    }

    public int getAnoFabricacao() {
        return anoFabricacao;
    }

    public void setAnoFabricacao(int anoFabricacao) {
        this.anoFabricacao = anoFabricacao;
    }

    public int calculaGarantia() {
        int anosDeGarantia = 2;
        return anoFabricacao + anosDeGarantia;
    }
}
