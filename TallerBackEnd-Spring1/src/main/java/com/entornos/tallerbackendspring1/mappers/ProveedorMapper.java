package com.entornos.tallerbackendspring1.mappers;

import com.entornos.tallerbackendspring1.DTO.ProveedorDTO;
import com.entornos.tallerbackendspring1.model.Proveedor;
import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

@Mapper(componentModel = "spring")
public interface ProveedorMapper {
    ProveedorMapper INSTANCE= Mappers.getMapper(ProveedorMapper.class);
    ProveedorDTO toProveedorDTO(Proveedor proveedor);

    Proveedor toProveedor(ProveedorDTO proveedorDTO);
}
