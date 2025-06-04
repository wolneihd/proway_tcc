package com.proway.backend.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.proway.backend.models.Categoria;
import com.proway.backend.services.CategoriasService;

@RestController
@RequestMapping(value = "/categorias")
public class CategoriasController {
    
    @Autowired
    private CategoriasService categoriasService;

    @GetMapping
    public ResponseEntity<List<Categoria>> getAllCategorias() {
        List<Categoria> categorias = categoriasService.findAll();
        return ResponseEntity.ok().body(categorias);
    }

}
