public class Servico {
    private int ID;
    private String motivo;
    private Mecanico mecanico;
    private Veiculo veiculo;

    public Servico(int ID, Mecanico mecanico, Veiculo veiculo) {
        this.ID = ID;
        this.motivo = null;
        this.mecanico = mecanico;
        this.veiculo = veiculo;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public Mecanico getMecanico() {
        return mecanico;
    }

    public void setMecanico(Mecanico mecanico) {
        this.mecanico = mecanico;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public void setVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }

    public void ordemServico(String motivo) {
        this.motivo = motivo;
        veiculo.setNumOcorrencias(veiculo.getNumOcorrencias() + 1);
    }
}
