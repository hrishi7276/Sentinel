using Microsoft.AspNetCore.Mvc;
using Sentinel.Web.Services.Engine;

namespace Sentinel.Web.Controllers;

public class EngineController : Controller
{
    private readonly IEngineClient _engineClient;

    public EngineController(IEngineClient engineClient)
    {
        _engineClient = engineClient;
    }

    public async Task<IActionResult> Health()
    {
        var health = await _engineClient.GetHealthAsync();

        return View(health);
    }
}