CREATE VIEW [dbo].[v_UsuariosActivos]
AS
SELECT 
    [UsuarioId],
    [Nombre],
    [Email],
    [FechaCreacion]
FROM [dbo].[Usuarios]
WHERE [Activo] = 1;
