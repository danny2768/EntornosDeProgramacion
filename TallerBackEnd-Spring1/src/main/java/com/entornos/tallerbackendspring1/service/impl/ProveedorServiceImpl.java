package com.entornos.tallerbackendspring1.service.impl;

import com.entornos.tallerbackendspring1.DTO.ProveedorDTO;
import com.entornos.tallerbackendspring1.mappers.ProveedorMapper;
import com.entornos.tallerbackendspring1.model.Proveedor;
import com.entornos.tallerbackendspring1.repository.IProveedorRepository;
import com.entornos.tallerbackendspring1.service.interfaces.IProveedorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProveedorServiceImpl implements IProveedorService{
    private IProveedorRepository proveedorRepository;

    @Override
    public List<ProveedorDTO> getProveedores(){
        List<Proveedor>proveedorList = proveedorRepository.findAll();
        return proveedorList.stream().map(ProveedorMapper.INSTANCE::toProveedorDTO).collect(Collectors.toList());
    }

    @Override
    public ProveedorDTO getProveedorById(Long id_proveedor) {
        Proveedor proveedor = proveedorRepository.findById(Math.toIntExact(id_proveedor)).orElse(null);
        return ProveedorMapper.INSTANCE.toProveedorDTO(proveedor);
    }

    @Override
    public ProveedorDTO createProveedor(ProveedorDTO proveedor) {
        Proveedor newProveedor = ProveedorMapper.INSTANCE.toProveedor(proveedor);
        newProveedor = proveedorRepository.save(newProveedor);
        return ProveedorMapper.INSTANCE.toProveedorDTO(newProveedor);
    }

    @Override
    public ProveedorDTO updateProveedor(Long id_proveedor, ProveedorDTO updatedProveedor) {
        Proveedor existingProveedor = proveedorRepository.findById(Math.toIntExact(id_proveedor))
                .orElse(null);

        if (existingProveedor != null) {
            // Update the fields of the existing supplier entity
            existingProveedor.setCiudad(updatedProveedor.getCiudad());
            existingProveedor.setDireccion(updatedProveedor.getDireccion());
            existingProveedor.setNombre(updatedProveedor.getNombre());
            existingProveedor.setTelefono(updatedProveedor.getTelefono());
            existingProveedor.setNit(updatedProveedor.getNit());

            // Save the updated supplier entity
            existingProveedor = proveedorRepository.save(existingProveedor);

            return ProveedorMapper.INSTANCE.toProveedorDTO(existingProveedor);
        } else {
            return null; // Supplier with the given ID not found
        }
    }

    @Override
    public Boolean deleteProveedor(Long id_proveedor) {
        if (proveedorRepository.existsById(Math.toIntExact(id_proveedor))) {
            proveedorRepository.deleteById(Math.toIntExact(id_proveedor));
            return true;
        } else {
            return false; // Supplier with the given ID not found
        }
    }

    @Autowired
    public void setProveedorRepository(IProveedorRepository proveedorRepository) {
        this.proveedorRepository = proveedorRepository;
    }
}