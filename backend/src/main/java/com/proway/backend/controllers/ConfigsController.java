package com.proway.backend.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.proway.backend.models.Configs;
import com.proway.backend.services.ConfigsService;

@RestController
@RequestMapping(value = "/configs")
public class ConfigsController {
    
    @Autowired
    private ConfigsService configsService;

    @GetMapping
    public ResponseEntity<Configs> getConfig() {
        Configs configs = configsService.findFirst();
        return ResponseEntity.ok().body(configs);
    }

    @PostMapping
    public ResponseEntity<Configs> atualizarDados(@RequestBody Configs configs) {
        Configs newConfig = configsService.updateConfigs(configs);
        return ResponseEntity.status(HttpStatus.CREATED).body(newConfig);
    }

}
