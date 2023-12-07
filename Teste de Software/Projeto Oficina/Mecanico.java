import java.util.List;

public class Mecanico {
    private String matricula;
    private String nome;
    private List<String> especialidades;

    public Mecanico(String matricula, String nome, List<String> especialidades) {
        this.matricula = matricula;
        this.nome = nome;
        this.especialidades = especialidades;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public List<String> getEspecialidades() {
        return especialidades;
    }

    public void setEspecialidades(List<String> especialidades) {
        this.especialidades = especialidades;
    }

    public boolean funcionarioPremium() {
        return especialidades.size() > 1;
    }
}
