package com.proway.backend.models;

import java.time.Instant;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import com.proway.backend.enums.TipoMensagem;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "mensagem")
public class Mensagem {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autoincrementado
    private Long id;

    @Enumerated(EnumType.STRING)
    private TipoMensagem tipoMensagem;

    private boolean respondido;
    private String textoMensagem;
    private String caminhoArquivo;
    private String resposta;

    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss'Z'", timezone = "GMT")
    private Instant instant;

    @OneToOne(mappedBy = "mensagem", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JsonManagedReference("mensagem-analise") 
    private Analise analise;

    @ManyToOne
    @JoinColumn(name = "usuario_id", nullable = false)
    @JsonBackReference("usuario-mensagens")
    private Usuario usuario;

    public Mensagem() { }

    public Mensagem(Long id, TipoMensagem tipoMensagem, boolean respondido, String textoMensagem,
            String caminhhoArquivo, String resposta, Instant instant, Analise analise, Usuario usuario) {
        this.id = id;
        this.tipoMensagem = tipoMensagem;
        this.respondido = respondido;
        this.textoMensagem = textoMensagem;
        this.caminhoArquivo = caminhhoArquivo;
        this.resposta = resposta;
        this.instant = instant;
        this.analise = analise;
        this.usuario = usuario;
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

    public TipoMensagem getTipoMensagem() {
        return tipoMensagem;
    }

    public void setTipoMensagem(TipoMensagem tipoMensagem) {
        this.tipoMensagem = tipoMensagem;
    }

    public boolean isRespondido() {
        return respondido;
    }

    public void setRespondido(boolean respondido) {
        this.respondido = respondido;
    }

    public String getTextoMensagem() {
        return textoMensagem;
    }

    public void setTextoMensagem(String textoMensagem) {
        this.textoMensagem = textoMensagem;
    }

    public String getCaminhhoArquivo() {
        return caminhoArquivo;
    }

    public void setCaminhhoArquivo(String caminhoArquivo) {
        this.caminhoArquivo = caminhoArquivo;
    }

    public String getResposta() {
        return resposta;
    }

    public void setResposta(String resposta) {
        this.resposta = resposta;
    }

    public Instant getInstant() {
        return instant;
    }

    public void setInstant(Instant instant) {
        this.instant = instant;
    }

    public Analise getAnalise() {
        return analise;
    }

    public void setAnalise(Analise analise) {
        this.analise = analise;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }
}
