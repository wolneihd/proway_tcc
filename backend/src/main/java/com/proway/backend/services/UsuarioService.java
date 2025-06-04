package com.proway.backend.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.proway.backend.models.Analise;
import com.proway.backend.models.Mensagem;
import com.proway.backend.models.Usuario;
import com.proway.backend.repositories.MensagemRepository;
import com.proway.backend.repositories.UsuarioRepository;

@Service
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private MensagemRepository mensagemRepository;

    public List<Usuario> findAll() {
        return usuarioRepository.findAll();
    }

    public Usuario saveInput(Usuario usuario) {
        if (usuario == null) {
            throw new IllegalArgumentException("Usuário não pode ser nulo");
        }
    
        // Verifica se já existe
        if (usuarioRepository.existsByIdTelegram(usuario.getIdTelegram())) {
            Usuario usuarioExistente = usuarioRepository.findByIdTelegram(usuario.getIdTelegram());
    
            List<Mensagem> listaMensagens = usuario.getMensagens();
            if (listaMensagens != null && !listaMensagens.isEmpty()) {
                Mensagem novaMensagem = listaMensagens.get(0);
                novaMensagem.setUsuario(usuarioExistente); // associa a mensagem ao usuário existente
    
                Analise analise = novaMensagem.getAnalise();
                if (analise != null) {
                    analise.setMensagem(novaMensagem);         // vínculo bidirecional obrigatório
                    novaMensagem.setAnalise(analise);          // redundante mas seguro
                }
    
                mensagemRepository.save(novaMensagem);         // Cascade salva a analise
            }
    
            return usuarioExistente;
        }
    
        // Novo usuário com mensagens (e análises)
        List<Mensagem> mensagens = usuario.getMensagens();
        if (mensagens != null) {
            for (Mensagem m : mensagens) {
                m.setUsuario(usuario);
    
                Analise a = m.getAnalise();
                if (a != null) {
                    a.setMensagem(m); // <- ESSENCIAL
                    m.setAnalise(a);
                }
            }
        }
    
        return usuarioRepository.save(usuario);
    }

}
