package com.entornos.tallerbackendspring1.controller;

import com.entornos.tallerbackendspring1.DTO.ProveedorDTO;
import com.entornos.tallerbackendspring1.service.interfaces.IProveedorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/public/api/proveedores")
public class ProveedorController {
    private IProveedorService proveedorService;

    @GetMapping
    public ResponseEntity<List<ProveedorDTO>> getProveedores(){
        return ResponseEntity.ok(proveedorService.getProveedores());
    }

    @GetMapping("/{id_proveedor}")
    public ResponseEntity<ProveedorDTO> getProveedorById(@PathVariable Long id_proveedor){
        ProveedorDTO proveedorDTO = this.proveedorService.getProveedorById(id_proveedor);
        return ResponseEntity.ok(proveedorDTO);
    }

    @PostMapping("/create")
    public ResponseEntity<ProveedorDTO> createProveedor(@RequestBody ProveedorDTO proveedorDTO) {
        ProveedorDTO createdProveedor = proveedorService.createProveedor(proveedorDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdProveedor);
    }

    @PutMapping("/{id_proveedor}")
    public ResponseEntity<ProveedorDTO> updateProveedor(@PathVariable Long id_proveedor, @RequestBody ProveedorDTO proveedorDTO) {
        ProveedorDTO updatedProveedor = proveedorService.updateProveedor(id_proveedor, proveedorDTO);
        if (updatedProveedor != null) {
            return ResponseEntity.ok(updatedProveedor);
        } else {
            return ResponseEntity.notFound().build(); // Return 404 if supplier is not found
        }
    }

    @DeleteMapping("/{id_proveedor}")
    public ResponseEntity<Boolean> deleteProveedor(@PathVariable Long id_proveedor){
        return ResponseEntity.ok(proveedorService.deleteProveedor(id_proveedor));
    }

    @Autowired
    public void setProveedorService(IProveedorService proveedorService){
        this.proveedorService = proveedorService;
    }

}
