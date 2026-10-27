CREATE PROCEDURE [dbo].[sp_ObtenerUsuarioPorId]
    @UsuarioId INT
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        [UsuarioId],
        [Nombre],
        [Email],
        [Telefono],
        [Activo]
    FROM [dbo].[Usuarios]
    WHERE [UsuarioId] = @UsuarioId;
END;
