package com.entornos.tallerbackendspring1.service.interfaces;

import com.entornos.tallerbackendspring1.DTO.ProveedorDTO;

import java.util.List;

public interface IProveedorService {

    List<ProveedorDTO> getProveedores();

    ProveedorDTO getProveedorById(Long id_proveedor);

    ProveedorDTO createProveedor(ProveedorDTO proveedor);

    ProveedorDTO updateProveedor(Long id_proveedor, ProveedorDTO proveedor);

    Boolean deleteProveedor(Long id_proveedor);




}
