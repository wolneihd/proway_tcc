package com.proway.backend.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.proway.backend.models.Usuario;
import com.proway.backend.services.UsuarioService;

@RestController
@RequestMapping(value = "/")
public class UsuarioController {
    
    @Autowired
    private UsuarioService usuarioService;

    @GetMapping
    public ResponseEntity<List<Usuario>> findAll() {
        List<Usuario> listaUsuarios = usuarioService.findAll(); 
        return ResponseEntity.ok().body(listaUsuarios);
    }

    @PostMapping
    public ResponseEntity<Usuario> salvarInput(@RequestBody Usuario usuario) {
        Usuario salvo = usuarioService.saveInput(usuario);
        return ResponseEntity.status(HttpStatus.CREATED).body(salvo);
    }
}
