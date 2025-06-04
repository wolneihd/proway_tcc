package com.proway.backend.models;

import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonManagedReference;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

@Entity
@Table(name = "usuario")
public class Usuario {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autoincrementado
    private Long id;

    private Long idTelegram;
    private String nome;
    private String sobrenome;
    
    @OneToMany(mappedBy = "usuario", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference("usuario-mensagens")
    private List<Mensagem> mensagens = new ArrayList<>();

    public Usuario() { }

    public Usuario(Long id, Long idTelegram, String nome, String sobrenome, List<Mensagem> mensagens) {
        this.id = id;
        this.idTelegram = idTelegram;
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.mensagens = mensagens;
    }

    public static long getSerialversionuid() {
        return serialVersionUID;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getIdTelegram() {
        return idTelegram;
    }

    public void setIdTelegram(Long idTelegram) {
        this.idTelegram = idTelegram;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public List<Mensagem> getMensagens() {
        return mensagens;
    }
}
