import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'providers/app_provider.dart';
import 'utils/theme.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();
  runApp(
    ChangeNotifierProvider(
      create: (_) => AppProvider()..init(),
      child: const BudgetFlowApp(),
    ),
  );
}

class BudgetFlowApp extends StatelessWidget {
  const BudgetFlowApp({super.key});

  @override
  Widget build(BuildContext context) {
    final prov = context.watch<AppProvider>();
    return MaterialApp(
      title: 'Budget Flow',
      debugShowCheckedModeBanner: false,
      theme: lightTheme(prov.isAr),
      darkTheme: darkTheme(prov.isAr),
      themeMode: prov.isDark ? ThemeMode.dark : ThemeMode.light,
      home: prov.isLoggedIn ? const HomeScreen() : const LoginScreen(),
    );
  }
}
