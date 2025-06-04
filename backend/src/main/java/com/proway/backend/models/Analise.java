package com.proway.backend.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.proway.backend.enums.LLM;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "analise")
public class Analise {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autoincrementado
    private Long id;

    @Enumerated(EnumType.STRING)
    private LLM llm;

    private String feedback;
    private String resumo;
    private String resposta;
    private String categoria;

    @OneToOne
    @JoinColumn(name = "mensagem_id")
    @JsonBackReference("mensagem-analise") 
    private Mensagem mensagem;

    public Analise() { }

    public Analise(Long id, LLM llm, String feedback, String categoria, String resumo, String resposta, Mensagem mensagem) {
        this.id = id;
        this.llm = llm;
        this.feedback = feedback;
        this.categoria = categoria;
        this.resumo = resumo;
        this.resposta = resposta;
        this.mensagem = mensagem;
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

    public LLM getLlm() {
        return llm;
    }

    public void setLlm(LLM llm) {
        this.llm = llm;
    }

    public String getFeedback() {
        return feedback;
    }

    public void setFeedback(String feedback) {
        this.feedback = feedback;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getResumo() {
        return resumo;
    }

    public void setResumo(String resumo) {
        this.resumo = resumo;
    }

    public String getResposta() {
        return resposta;
    }

    public void setResposta(String resposta) {
        this.resposta = resposta;
    }

    public Mensagem getMensagem() {
        return mensagem;
    }

    public void setMensagem(Mensagem mensagem) {
        this.mensagem = mensagem;
    }

    
    
}
